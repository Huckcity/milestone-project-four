import pymysql, logging

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
        
    def add_recipe(self, title, category, serves, description, recipeGF, recipeVegan, username, ingredients):
        
        userID = self.get_user_id(username)
        description = description.strip("',/\n")
        
        try:
            
            sql = ("INSERT INTO recipes (recipeName, recipeCategory, recipeServes, recipeDesc, recipeAdded, recipeGF, recipeVegan, recipeAuthor) VALUES (%s, %s, %s, %s, NOW(), %s, %s, %s)")
            vals = (title, category, serves, description, recipeGF, recipeVegan, userID)
            self.cur.execute(sql, vals)
            
            recipeID = self.cur.lastrowid
            
            for ingredient, quantity in ingredients.items():
                
                try:
                    
                    sql = ("INSERT INTO recipeingredients (recipeID, ingredientID, riQuantity) VALUES (%s, %s, %s)")
                    vals = (recipeID, ingredient, quantity)
                    self.cur.execute(sql, vals)
                    
                except pymysql.Error as error :
                    
                    print(error)
                    self.con.rollback() #rollback if any exception occured
                    result = False
                    
            self.con.commit()
                    
            result = True
            
        except pymysql.Error as error :
            
            print(error)
            self.con.rollback() #rollback if any exception occured
            result = False
            
        return result
        
    def get_user_id(self, username):
    
        sql = ("SELECT userID FROM users where userName = %s")
        vals = (username)
        self.cur.execute(sql, vals)
        result = self.cur.fetchone()
        return result['userID']
        
    def get_categories(self):
        
        sql = ("SELECT * FROM categories")
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
        
    def get_ingredients(self):
        
        sql = ("SELECT * FROM ingredients")
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
        
    def get_recipe(self, recipeID):
        
        sql = ("SELECT * FROM recipes WHERE recipeID = %s")
        vals = recipeID
        self.cur.execute(sql, vals)
        result = self.cur.fetchone()
        return result