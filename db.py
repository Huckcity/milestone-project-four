import pymysql

class Database:
    
    def __init__(self):
        host = "sql2.freesqldatabase.com"
        user = "sql2278391"
        password = "zW4!eF6%"
        db = "sql2278391"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()
    
    def list_recipes(self):
        self.cur.execute("SELECT * FROM recipes")
        result = self.cur.fetchall()
        return result