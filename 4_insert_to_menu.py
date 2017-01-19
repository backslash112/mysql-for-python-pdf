import MySQLdb as mysql

mydb = mysql.connect(host="localhost",
                           user="root",
                           passwd="123456",
                           db="menu")
cur = mydb.cursor()
statement = """insert into fish(name, price) values("shark", "13.00")"""
cur.execute(statement)
