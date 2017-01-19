import sys
import MySQLdb as mysql

def main():
    # create a connection object
    connection = mysql.connect(host="localhost",
                               user="root",
                               passwd="123456",
                               db="menu")
    # create a cursor object
    cursor = connection.cursor()
    try:
        sql = "SELECT * FROM fish"
        result = cursor.execute(sql)
        print result
        results = cursor.fetchall()
        print results
    finally:
        connection.close()

if __name__ == "__main__":
    main()
