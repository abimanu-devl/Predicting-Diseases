#
# @author Wickramasekara T.M.A.M
# @email it19016962@my.sliit.lk
#

import pymysql

# Database Configuration
DATABASE = "cxr_scan"
HOST = "cxr-database.czbmndal6xg0.us-east-1.rds.amazonaws.com"
USER = "cxr_user"
PASS = "cxr_user"
db = pymysql.connect(database=DATABASE, host = HOST, user = USER, password = PASS)

cursor = db.cursor() # To execute sql queries

# Insert Data Function
def insert(sql_query, args):
    try:
        cursor.execute(sql_query, args)
        db.commit()
        return args
    except Exception as e:
        db.rollback()
        db.close()
        print(e)
        return e
