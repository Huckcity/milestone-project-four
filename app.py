import os
from flask import Flask, render_template
import pymysql

app = Flask(__name__)

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

@app.route("/")
def main():
    
    def db_query():
        db = Database()
        recipes = db.list_recipes()
        return recipes
    
    results = db_query()
    
    return render_template('index.html', result=results)
  
if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)