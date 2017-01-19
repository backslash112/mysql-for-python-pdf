#!/usr/bin/env python

import sys
import getpass, MySQLdb, optparse, string


def valid_digit(value):
    if value.isdigit() is not True:
        value = query(query, "digit")
    else:
        value = value
    return value

def valid_string(value):
    if value.isalpha() is not True:
        value = query(query, "alpha")
    else:
        value = value
    return value

def valid_table(choice, tables):
    valid_choice = valid_digit(choice) # Check whether the choice is a valid number
    valid_choice = int(valid_choice)
    while (valid_choice <= 0) or (valid_choice > len(tables)):
        # Ensure the choice is among the valid options
        print "Your selection is outside the bounds of possible chices."
        valid_choice = query(valid_choice, "digit")
    return valid_choice

def query(value, type):
    if type == "alpha":
        print "The value you entered ('%s') is not correct. "\
        "Please enter a valid value." % (value)
        new_value = raw_input("New value: ")
        valid_string(new_value)
        return new_value

    elif type == "digit":
        print "The value you entered ('%s') is not correct. "\
        "Please enter a valid value." % (value)
        new_value = raw_input("New value: ")
        valid_digit(new_value)
        return new_value

    else:
    ## if type  is neither "alpha" nor "digit"
        return 1

def main():
    # optparse
    opt = optparse.OptionParser()
    opt.add_option("-d", "--database", action="store", type="string", dest="database")
    opt.add_option("-p", "--passwd", action="store", type="string", dest="passwd")
    opt.add_option("-u", "--user", action="store", type="string", dest="user")
    opt, orgs = opt.parse_args()
    database = opt.database
    passwd = opt.passwd
    user = opt.user

    for i in (database, passwd, user):
        print "'%s'" % (i)

    while (user == "") or (user == None):
        print "This system is secured agianst anonymous loginis."
        user = getpass.getuser()

    while (passwd == "") or (passwd == None):
        print "You must have a valid password to log into the database."
        passwd = getpass.getpass()

    while (database =="") or (database == None):
        database = raw_input("We need the name of the an existing database" \
        " to proceed. Please enter it here: ")

    try:
        mydb = MySQLdb.connect(host = "localhost",
                               user = user,
                               passwd = passwd,
                               db = database)
        cur = mydb.cursor()
        quit = 1
    except Exception as e:
        print "The login credentials you entered are not valid for the database " \
        "you indicated. Please check your login details and try again."
        quit = 0
    finally:
        pass

    if quit == 1:
        # show the table list
        get_tables_statement = """Show tables"""
        cur.execute(get_tables_statement)
        tables = cur.fetchall()
        print "The tables avaliable for database %s follow below: " % (database)
        for i in xrange(0, len(tables)):
            print "%s. %s" % (i+1, tables[i])

        # ask the user to choice the table
        table_choice = raw_input("Please enter the number of the table into "\
        "which you would like to insert data. ")

        # valid the user input for table
        table_choice = str(table_choice)
        table_no = valid_table(table_choice, tables)
        table = tables[table_no-1][0]

        # show the table structure
        show_def = raw_input("Would you like to seee the database structure of "\
        "the table '%s'? (y/n)" % (table))
        if show_def == "y":
            def_statement = """describe %s""" % (table)
            cur.execute(def_statement)
            definition = cur.fetchall()
            from prettytable import PrettyTable
            # tabledef = PrettyTable()
            # tabledef.set_field_names(["Field", "Type", "Null", "Key", "Default", "Extra"])
            tabledef = PrettyTable(["Field", "Type", "Null", "Key", "Default", "Extra"])
            for j in xrange(0, len(definition)):
                tabledef.add_row([definition[j][0], definition[j][1],
                                  definition[j][2], definition[j][3],
                                  definition[j][4], definition[j][5]])
            # tabledef.printt()
            print tabledef

        # accepting user input for the INSERT statement
        print "Please enter the data you would like to insert into table %s" % (table)
        columns = []
        values = []
        for j in xrange(0, len(definition)):
            column = definition[j][0]
            value = raw_input("Value to insert for column '%s'?" % (definition[j][0]))
            columns.append(str(column))
            values.append('"' + str(value) + '"')
        columns = ','.join(columns)
        values = ','.join(values)
        print columns
        print values

        # building the INSERT statement form the user input and executing it
        statement = """insert into %s(%s) values(%s)""" % (table, columns, values)
        try:
            cur.execute(statement)
        except Exception as e:
            raise
        finally:
            print "Data has been inserted using the following statement:\n", statement
            cur.close()
            mydb.commit()
            mydb.close()

if __name__ == "__main__":
    main()
