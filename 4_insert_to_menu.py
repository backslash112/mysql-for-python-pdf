import MySQLdb as mysql
import sys

def valid_name(name):
    if name.isalpha() is False:
        fish = query("name", name, "alpha")
    else:
        fish = name
    return fish

def valid_price(price):
    if price.isdigit() is False:
        price = query("price", price, "digit")
    else:
        price = price
    return price

def query(column, value, kind):
    if kind == "alpha":
        print "For %s, you input %s. This is not a valid value for column %s. " \
        "Please enter the name of the fish in the appropriate format." \
         % (column, value, column)
        new_value = raw_input("New name:")
        new_value = valid_name(new_value)
        return (new_value)
    elif kind == "digit":
        print "For %s, you input %s. This is not a valid price. Please enter" \
        " the price in the appropriate format." % (column, value)
        new_price = raw_input("New price:")
        new_price = valid_price(new_price)
        return (new_price)
    else:
        return -1
        
mydb = mysql.connect(host="localhost",
                           user="root",
                           passwd="123456",
                           db="menu")
cur = mydb.cursor()
fish = sys.argv[1]
price = sys.argv[2]

# passing fish and price for validation
fish = valid_name(fish)
price = valid_price(price)

statement = """insert into fish(name, price) values('%s', %s)""" % (fish, price)
try:
    cur.execute(statement)
    mydb.commit()
finally:
    mydb.close()
