#! usr/bin/env python

# p177 Project: Bad apples

import MySQLdb, optparse, sys
import smtplib

# Get options
opt = optparse.OptionParser()
opt.add_option("-i", "--insert", action="store_true", help="flag request for "\
"insertion - only ONE of insert, update, or select can be used at a time", dest="insert")
opt.add_option("-u", "--update", action="store_true", help="flag request as an update", dest="update")
opt.add_option("-s", "--select", action="store_true", help="flag request as a selection", dest="select")
opt.add_option("-d", "--database", action="store", type="string", help="name of the local database", dest="database")
opt.add_option("-t", "--table", action="store", type="string", help="table in the indicated database", dest="table")
opt.add_option("-c", "--columns", action="store", type="string", help="column(s) of the indicated table", dest="columns")
opt.add_option("-v", "--values", action="store", type="string", help="vlues to be processed", dest="values")
opt, args = opt.parse_args()

# Only one kind of statement is allowed. If more than one is indicated, the priority
# of assignment is SELECT -> UPDATE -> INSERT.
if opt.select is True:
    statement_type = "select"
elif opt.update is True:
    statement_type = "update"
elif opt.insert is True:
    statement_type = "insert"

database = opt.database
table = opt.table
columns = opt.columns
values = opt.values

def connection(database):
    """Create a database connection and returns the cursor. Host is hardwired to 'localhost'"""
    try:
        mydb = MySQLdb.connect(host = "localhost",
                               user = "root",
                               passwd = "123456",
                               db = database)
        cur = mydb.cursor()
        return cur
    except MySQLdb.Error:
        print "There was a problem in connecting to the database. Please ensure that"\
        "the database exists on the local host system."
        raise MySQLdb.Error
    except MySQLdb.Warning:
        pass

def sendmail(message, recipient):
    """Sends mail through localhost. Takes error message and intended recipient as arguments"""

    fromadds = "yangcun@live.com"
    toadds = "459455120@qq.com"

    # Add the From: and To: headers at the start!
    msg = "From: %s\r\n To: %s\r\n\r\n" % (fromadds, toadds)
    msg = msg + str(message[0] + message[1])

    server = smtplib.SMTP('localhost')
    server.set_debuglevel(1)
    server.sendmail(fromadds, toadds, msg)
    server.quit()

class MySQLStatement:
    def __init__(self):
        """Creates an instance to form and execute a MySQL statement"""
        self.Statement = []

    def type(self, kind):
        """Indicates the type of statement that the instance is. Supported "\
        "types are select, insert and update. This is must be set before "\
        "using any of the object methods."""
        self.type = kind

    def form(self, table, column, info):
        """Forms the MySQL statement according to the type of statement, "\
        "using table as the tablename, column for the fields, and info for values"""
        data = info.split(',')
        value = "'" + data[0]
        for i in range(1, len(data)):
            value = value + "', '" + data[i]
        value = value+ "'"

        if self.type == "select":
            statement = """select * from %s where %s=%s""" % (table, column, value)
            return statement
        elif self.type == "insert":
            statement = """insert into %s(%s) values(%s)""" % (table, column, value)
            return statement
        elif self.type == "update":
            statement = """update %s set %s=%s where %s=%s""" % (table, column, data[0], column, data[1])
            return statement

    def execute(self, statement, table, cursor):
        print "execute()"
        """Attempts execution of the statement resulting from MySQLStatement.form()."""
        while True:
            try:
                print "\nTrying SQL statement: %s\n\n" % (statement)
                cursor.execute(statement)

                if self.type == "select":
                    # Run query
                    output = cursor.fetchall()

                    results = ""
                    data = ""
                    for record in output:
                        for entry in record:
                            data = data + '\t' + str(entry)
                        data = data + "\n"
                    results = results + data + "\n"
                    return results

                elif self.type == "insert":
                    results = "Your information was inserted with the "\
                    "following SQL statement: %s" % (statement)
                    return results
                elif self.type == "update":
                    results = "Your updated information in the database with "\
                    "the following SQL statement: %s" % (statement)
                    return results

            # OperationalError
            except MySQLdb.OperationalError, e:
                sendmail(e, "pythondevelopers")
                print "Some of the information you have passed is not valid. "\
                "Please check it before trying to use this program again. You "\
                "may also use '-h' to see the options avaliable."
                raise

            # DataError
            # ProgrammingError
            except (MySQLdb.DataError, MySQLdb.ProgrammingError), e:
                sendmail(e, "pythondevelopers")
                print "An irrecoverable error has occured in the way your data "\
                "was to be processed. This application must now close. An error "\
                "message describing the fault has been sent to the development "\
                "team. Apoligies for any inconvenience."
                raise

            # IntegrityError
            except MySQLdb.IntegrityError, e:
                sendmail(e, "dba")
                print "An irrecoverable database error has occurred and this "\
                "process must now end. An error message describing the fault "\
                "has been sent to the databaes administrator. Apologies for "\
                "any inconvenience."
                raise

            #InternalError
            # NotSupportedError
            except (MySQLdb.InternalError, MySQLdb.NotSupportedError), e:
                sendmail(e, "dba")
                sendmail(e, "pythondevelopers")
                print "An irrecoverable error has occurred and this process "\
                "must now end. An error message describing the fault has been "\
                "sent to the appropriate staff. Apologies for any inconvenience"
                raise

            except MySQLdb.Warning:
                pass

            finally:
                pass

def main():
    request = MySQLStatement()
    try:
        request.type(statement_type)
        phrase = request.form(table, columns, values)
        cur = connection(database)
        results = request.execute(phrase, table, cur)
        print "Results:\n", results
        cur.close()
    except MySQLdb.Error, e:
        sendmail(e, "pythondevelopers")
        print "The values you entered are not valid. Please check the "\
        "information you are using before try again."
        print "The SQL statement that was tried reads as follows: %s" % (statement)
        raise MySQLdb.Error

    except MySQLdb.Warning:
        pass

    finally:
        pass

if __name__ == "__main__":
    main()
