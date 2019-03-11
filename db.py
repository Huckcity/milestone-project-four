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
            
            print(error)
            self.con.rollback() #rollback if any exception occured
            result = False
            
        return result
        
    def find_user(self, username, password):
        try:
            
            sql = ("SELECT * FROM users where userName = %s AND userPassword = %s")
            vals = (username, password)
            self.cur.execute(sql, vals)
            result = self.cur.fetchone()
            print(result)
            return result
            
        except pymysql.Error as error :
            
            print(error)
            self.con.rollback() #rollback if any exception occured
            result = False
            
        return result
    
    def list_recipes(self):
        
        self.cur.execute("SELECT * FROM recipes")
        result = self.cur.fetchall()
        return result
        
    def list_recipes_by_ingredient(self, ingredientID):
        
        sql =("SELECT * FROM recipes r JOIN recipeingredients ri ON r.recipeID = ri.recipeID WHERE ri.ingredientID = %s")
        vals = (ingredientID)
        self.cur.execute(sql, vals)
        result = self.cur.fetchall()
        return result
        
    def add_recipe(self, title, category, serves, description, recipeGF, recipeVegan, username, ingredients):
        
        userID = self.get_user_id(username)
        title = title.encode('ascii', 'ignore')
        description = description.encode('ascii', 'ignore')
        
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
    
    def edit_recipe(self, title, category, serves, description, recipeGF, recipeVegan, username, ingredients, removedIngredients, recipeID):
        
        try:
        
            sql = ("UPDATE recipes SET recipeName = %s, recipeCategory = %s, recipeServes = %s, recipeDesc = %s, recipeGF = %s, recipeVegan = %s WHERE recipeID = %s")
            vals = (title, category, serves, description, recipeGF, recipeVegan, recipeID)
            self.cur.execute(sql, vals)
            self.con.commit()
            result = True
        
        except pymysql.Error as error :
                
            print(error)
            self.con.rollback() #rollback if any exception occured
            result = False

        if len(ingredients) >= 1:
            for ingredient, quantity in ingredients.items():
                    
                try:
                    
                    sql = ("INSERT INTO recipeingredients (recipeID, ingredientID, riQuantity) VALUES (%s, %s, %s)")
                    vals = (recipeID, ingredient, quantity)
                    self.cur.execute(sql, vals)
                    self.con.commit()
                    result = True
                    
                except pymysql.Error as error :
                    
                    print(error)
                    self.con.rollback() #rollback if any exception occured
                    result = False
        
        
        print(removedIngredients)
        if len(removedIngredients) >= 1:
            for ingredient in removedIngredients:
                
                try:
                    
                    sql = ("DELETE FROM recipeingredients WHERE recipeID = %s AND ingredientID = %s LIMIT 1")
                    print(sql)
                    vals = (recipeID, ingredient)
                    self.cur.execute(sql, vals)
                    self.con.commit()
                    
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
        if result is not None:
            return result['userID']
        else:
            return False
        
    def get_categories(self):
        
        sql = ("SELECT * FROM categories")
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
        
    def get_ingredients(self):
        
        sql = ("SELECT * FROM ingredients ORDER BY ingredientName")
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
        
    def get_ingredients_for_recipe(self, recipeID):
        sql = ("SELECT * FROM ingredients i INNER JOIN recipeingredients ri ON i.ingredientID = ri.ingredientID WHERE ri.recipeID = %s")
        vals = recipeID
        self.cur.execute(sql, vals)
        result = self.cur.fetchall()
        return result
        
    def get_recipe(self, recipeID):
        
        sql = ("SELECT * FROM recipes WHERE recipeID = %s")
        vals = recipeID
        self.cur.execute(sql, vals)
        result = self.cur.fetchone()
        return result
        
    def add_ingredient(self, ingredient):
        
        try:
            
            sql = ("INSERT INTO ingredients (ingredientName) VALUES (%s)")
            vals = (ingredient)
            self.cur.execute(sql, vals)
            self.con.commit()
            result = True
            
        except pymysql.Error as error :
            
            print(error)
            self.con.rollback() #rollback if any exception occured
            result = False
            
        return result
        
    def get_common_ingredients(self):
        
        try:
            
            sql = ("SELECT ri.ingredientID, i.ingredientName, COUNT(ri.ingredientID) AS numOccurances FROM recipeingredients ri JOIN ingredients i ON ri.ingredientID = i.ingredientID GROUP BY ri.ingredientID ORDER BY numOccurances DESC LIMIT 5")
            self.cur.execute(sql)
            result = self.cur.fetchall()
            return result
            
        except pymysql.Error as error :
            
            print(error)
            self.con.rollback() #rollback if any exception occured
            result = False
            
        return result
        
    def add_view(self, recipeID):
        
        try:
            
            sql = ("UPDATE recipes SET recipeViews = recipeViews + 1 WHERE recipeID = %s")
            vals = (recipeID)
            self.cur.execute(sql, vals)
            self.con.commit()
            result = True
            
        except pymysql.Error as error :
            
            print(error)
            self.con.rollback() #rollback if any exception occured
            result = False
            
        return result
        
    def delete_recipe(self, recipeID):
        
        try:
            
            sql = ("DELETE FROM recipes WHERE recipeID = %s LIMIT 1")
            vals = (recipeID)
            self.cur.execute(sql, vals)
            self.con.commit()
            
            sql = ("DELETE FROM recipeingredients WHERE recipeID = %s LIMIT 1")
            vals = (recipeID)
            self.cur.execute(sql, vals)
            self.con.commit()
            
            sql = ("DELETE FROM likedrecipes WHERE recipeID = %s LIMIT 1")
            vals = (recipeID)
            self.cur.execute(sql, vals)
            self.con.commit()
            
            result = True
            
        except pymysql.Error as error :
            
            print(error)
            self.con.rollback() #rollback if any exception occured
            result = False
            
        return result
        
    def add_like(self, userID, recipeID):
        
        try:
            
            sql = ("SELECT * FROM likedrecipes WHERE userID = %s AND recipeID = %s")
            vals = (userID, recipeID)
            rows = self.cur.execute(sql, vals)
            
            if rows > 0:
                print('false')
                return False
            
            self.con.commit()
            
        except pymysql.Error as error :
            
            print(error)
            self.con.rollback() #rollback if any exception occured
            result = False
        
        try:
            
            sql = ("UPDATE recipes SET recipeVotes = recipeVotes + 1 WHERE recipeID = %s")
            vals = (recipeID)
            self.cur.execute(sql, vals)
            self.con.commit()
            result = True
            
        except pymysql.Error as error :
            
            print(error)
            self.con.rollback() #rollback if any exception occured
            result = False
        
        try:
            
            sql = ("INSERT INTO likedrecipes (userID, recipeID) VALUES (%s, %s)")
            vals = (userID, recipeID)
            self.cur.execute(sql, vals)
            self.con.commit()
            result = True
            
        except pymysql.Error as error :
            
            print(error)
            self.con.rollback() #rollback if any exception occured
            result = False
            
        return result
        
        
    def get_liked_recipes(self, userID):
        
        sql = ("SELECT * FROM recipes r JOIN likedrecipes lr ON r.recipeID = lr.recipeID WHERE lr.userID = %s")
        vals = (userID)
        self.cur.execute(sql, vals)
        result = self.cur.fetchall()
        return result