import os
from flask import Flask, render_template, request, session, redirect, url_for
from db import *
import logging

app = Flask(__name__)
app.secret_key = "SECRETKEY"

def auth_check():
    
    return redirect(url_for('login'))

 ########### LOGIN PAGE ###########

@app.route("/login", methods=['POST', 'GET'])
def login():
    
    if request.method == "POST":
    
        uname = request.form['username']
        password = request.form['password']
        
        if Database().find_user(uname, password):
            
            session['user'] = uname
            session['userID'] = Database().get_user_id(uname)
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
    
    auth_check()
    
    categories = Database().get_categories()
    ingredients = Database().get_ingredients()
    
    if request.method == "POST":
    
        title = request.form['title']
        category = request.form['category']
        serves = request.form['serves']
        description = request.form['description']
        
        numIngredients = request.form['ingredientsCount']
        ingredientsDict = {}
        
        for i in range(1, int(numIngredients)+1):

            ingName = "ingredient" + str(i)
            ingQuanName = "iQ" + str(i)
            
            if ingName in request.form:
                ingredientID = request.form[ingName]
                ingredientQuantity = request.form[ingQuanName]

                ingredientsDict[ingredientID] = ingredientQuantity
        
        recipeGF = True if request.form.get('recipeGF') else False
        recipeVegan = True if request.form.get('recipeVegan') else False
        
        if Database().add_recipe(title, category, serves, description, recipeGF, recipeVegan, session['user'], ingredientsDict):
            
            return redirect(url_for('recipes'))
            
        else:
        
            return redirect(url_for('addrecipe'))
            
    else:
    
        return render_template('addrecipe.html', categories = categories, ingredients = ingredients)
    
    

########### STATIC PAGES ###########

@app.route("/recipes")
def recipes():
    
    if session.get('userID') is None:
        return redirect(url_for('login'))
        
    recipes = Database().list_recipes()
    
    return render_template('recipes.html', recipes = recipes, uname = session['user'], userID = session['userID'])
    
@app.route("/recipe")
def recipe():
    
    recipeID = request.args.get('recipeID')    
    recipe = Database().get_recipe(recipeID)
    
    return render_template('recipe.html', recipe = recipe)
    
@app.route("/editrecipe")
def editrecipe():
    
    recipeID = request.args.get('recipeID')    
    recipe = Database().get_recipe(recipeID)
    
    return render_template('editrecipe.html', recipe = recipe)
    
@app.route("/about")
def about():
    return render_template('about.html')
    
@app.route("/home")
def home():
    
    if session.get('userID') is None:
        return redirect(url_for('login'))
        
    return render_template('home.html', uname = session['user'], userID = session['userID'])


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