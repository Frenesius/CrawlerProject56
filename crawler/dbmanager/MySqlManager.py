__author__ = 'j'
import MySQLdb
class MySqlManager:
    host = "localhost"
    user = "user1"
    passwd = "user1"
    db = "hardwareprice"
    DATABASE_NAME = "hardwareprice"
    TABLE_PRICE = "hardwareprice"
    TABLE_PRICE_COLUMN1 = "ean"
    TABLE_PRICE_COLUMN2 = "price"
    TABLE_PRICE_COLUMN3 = "timestamp"


    def __init__(self):
        pass
    def openDb(self):
        db = MySQLdb.connect(host= self.host, # your host, usually localhost
                      user= self.user, # your username
                      passwd= self.passwd, # your password
                      db= self.db) # name of the data base
        return db


    def insertPrice(self, db, EAN, price, timestamp):
        isExecuted = False
        try:
            a = MySqlManager()
            cursor = db.cursor()
            query = "INSERT INTO "+a.TABLE_PRICE+" ("+a.TABLE_PRICE_COLUMN1+", "+a.TABLE_PRICE_COLUMN2+", "+a.TABLE_PRICE_COLUMN3+")\
                VALUES ('"+EAN+"', '"+price+"', '"+timestamp+"')"
            cursor.execute(query)
            b.commit()
            isExecuted = True
        except:
            isExecuted = False
        return isExecuted





