import pymysql

class Database:
    
    def __init__(self):
        host = "eu-cdbr-west-02.cleardb.net"
        user = "b0f4c5cc5bb9e5"
        password = "ff6aa9b1"
        db = "heroku_3d6b51f0846c02a"
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
            
        return result
        
    def get_user_id(self, username):
    
        sql = ("SELECT userID FROM users where userName = %s")
        vals = (username)
        self.cur.execute(sql, vals)
        result = self.cur.fetchone()
        return result['userID']