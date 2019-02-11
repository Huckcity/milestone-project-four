import os
from flask import Flask, render_template, request, session, redirect, url_for
from db import *

app = Flask(__name__)
app.secret_key = "SECRETKEY"

 ########### LOGIN PAGE ###########

@app.route("/login", methods=['POST', 'GET'])
def login():
    
    if request.method == "POST":
    
        uname = request.form['username']
        password = request.form['password']
        
        if Database().find_user(uname, password):
            
            session['user'] = uname
            return redirect(url_for('home'))
            
        else:
        
            return redirect(url_for('login'))
    
    else:
    
        return render_template('login.html')
        
########### LOGOUT PAGE ###########
    
@app.route("/logout")
def logout():
    
    for key in session.keys():
     session.pop(key)
     
    return redirect(url_for('main'))
        

########### SIGN UP PAGE ###########

@app.route("/signup", methods=['POST', 'GET'])
def signup():
    
    if request.method == "POST":
    
        username = request.form['username']
        password = request.form['password']
        
        if Database().add_user(username, password):
            
            session['user'] = username
            return redirect(url_for('home'))
            
        else:
        
            return redirect('/signup')
            
    else:
    
        return render_template('signup.html')
        
########### ADD RECIPES PAGE ###########

@app.route("/addrecipe", methods=['POST', 'GET'])
def addrecipe():
    
    if request.method == "POST":
    
        title = request.form['title']
        description = request.form['description']
        recipeGF = request.form.get['recipeGF']
        
        if Database().add_recipe(title, description, recipeGF, session['user']):

            return redirect(url_for('recipes'))
            
        else:
        
            return redirect(url_for('addrecipe'))
            
    else:
    
        return render_template('addrecipe.html')
    
    

########### STATIC PAGES ###########

@app.route("/recipes")
def recipes():
    
    recipes = Database().list_recipes()
    
    return render_template('recipes.html', recipes = recipes)
    
@app.route("/about")
def about():
    return render_template('about.html')
    
@app.route("/home")
def home():
    
    return render_template('home.html', uname = session['user'])


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