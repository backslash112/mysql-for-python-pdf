#!/usr/bin/env python
import MySQLdb as mysql

mydb = mysql.connect(host="localhost",
                           user="root",
                           passwd="123456",
                           db="world")
cur = mydb.cursor()

table = "City"
column = "Name"
term = 's%'
statement = """select * from %s where %s like '%s'""" % (table, column, term)

command = cur.execute(statement)
results = cur.fetchall()
# print results

record_list = []
for record in results:
    record_list.append(record[1])

for i in range(0, len(record_list)):
    print "%s. %s" % (i+1, record_list[i])
