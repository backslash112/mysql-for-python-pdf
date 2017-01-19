import MySQLdb as mysql
import sys

mydb = mysql.connect(host="localhost",
                           user="root",
                           passwd="123456",
                           db="menu")
cur = mydb.cursor()
fish = sys.argv[1]
price = sys.argv[2]
statement = """insert into fish(name, price) values('%s', %s)""" % (fish, price)

cur.execute(statement)
