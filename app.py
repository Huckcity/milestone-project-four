import os
from flask import Flask, render_template
from db import *

app = Flask(__name__)

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')
    
@app.route("/about")
def about():
    return render_template('about.html')
    


@app.route("/")
def main():
    
    def db_query():
        database = Database()
        recipes = database.list_recipes()
        return recipes
    
    results = db_query()
    
    return render_template('index.html', result=results)
  
if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)