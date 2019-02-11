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
    
    def add_user(self, username, password):
        try:
            
            self.cur.execute("INSERT INTO users (userName, userPassword, userJoined) VALUES ('"+username+"', '"+password+"', NOW())")
            self.con.commit()
            result = True
            
        except pymysql.Error as error :
            
            self.con.rollback() #rollback if any exception occured
            result = False
            
        return result
        
    def find_user(self, username, password):
        try:
            
            self.cur.execute("SELECT * FROM users where userName = 'username' AND userPassword = 'password'")
            self.con.commit()
            result = True
            
        except pymysql.Error as error :
            
            self.con.rollback() #rollback if any exception occured
            result = False
            
        return result
    
    def list_recipes(self):
        
        self.cur.execute("SELECT * FROM recipes")
        result = self.cur.fetchall()
        return result
        
    def add_recipe(self, title, description, recipeGF, username):
        
        userID = self.get_user_id(username)
        
        try:
            
            sql = ("INSERT INTO recipes (recipeName, recipeDesc, recipeAdded, recipeGF, recipeAuthor) VALUES (%s, %s, NOW(), %s, %s)")
            vals = (title, description, recipeGF, userID)
            self.cur.execute(sql, vals)
            self.con.commit()
            result = True
            
        except pymysql.Error as error :
            
            self.con.rollback() #rollback if any exception occured
            result = False
            print error
            
        return result
        
    def get_user_id(self, username):
    
        sql = ("SELECT userID FROM users where userName = %s")
        vals = (username)
        self.cur.execute(sql, vals)
        result = self.cur.fetchone()
        return result['userID']