#!/usr/bin/env python
import MySQLdb as mysql

mydb = mysql.connect(host="localhost",
                           user="root",
                           passwd="123456",
                           db="menu")
cur = mydb.cursor()

column = 'name'
term = 's%'
statement = """select %s from fish where name like '%s'""" % (column, term)
command = cur.execute(statement)
results = cur.fetchall()
print results

column_list = []
for record in results:
    column_list.append(record)

print "Did you mean:"
for i in xrange(0, len(column_list)):
    print "%s. %s" % (i+1, column_list[i])
option = raw_input('Number:')
intoption = int(option)
