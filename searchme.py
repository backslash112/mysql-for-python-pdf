#!/usr/bin/env python
import MySQLdb as mysql
import optparse

mydb = mysql.connect(host="localhost",
                           user="root",
                           passwd="123456",
                           db="menu")
cur = mydb.cursor()

column = 'name'
term = 's%'

# optparse
opt = optparse.OptionParser()
opt.add_option("-q", "--query", action="store", type="string", dest="term")
opt.add_option("-t", "--table", action="store", type="string", dest="table")
opt.add_option("-f", "--format", action="store_true", dest="format")
opt.add_option("-o", "--output", action="store", type="string", dest="outfile")
opt, args = opt.parse_args()
term = opt.term
form = opt.format
table = opt.table
outfile = opt.outfile

statement = """select * from fish where name like '%s'""" % (term)
command = cur.execute(statement)
results = cur.fetchall()

if form is True:
    columns_query = """DESCRIBE %s""" % (table)
    columns_command = cur.execute(columns_query)
    headers = cur.fetchall()
    # print headers
    column_list = []
    for record in headers:
        column_list.append(record[0])
    output = ""
    for record in results:
        print record
        output = output + "====================\n\n"
        for field_no in xrange(0, len(column_list)):
            output = output + column_list[field_no] + ": " + str(record[field_no]) + "\n"
        output = output + "\n"
        # print output
else:
    output = []
    for record in xrange(0, len(results)):
        output.append(results[record])

if outfile:
    out = open(outfile, 'w')
    out.write(output)
else:
    print output
