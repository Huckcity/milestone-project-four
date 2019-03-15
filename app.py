import os
from flask import Flask, render_template, request, session, redirect, url_for
import json
from db import *

app = Flask(__name__)
app.secret_key = "SECRETKEY"


 ########### LOGIN PAGE ###########

@app.route("/login", methods=['POST', 'GET'])
def login():
    
    if session.get('userID'):
        return redirect(url_for('home'))
    
    if request.method == "POST":
    
        uname = request.form['username']
        password = request.form['password']
        
        if Database().find_user(uname, password):
            
            session['user'] = uname
            session['userID'] = Database().get_user_id(uname)
            return redirect(url_for('home'))
            
        else:
        
            msg = "Please check your login details."
            return render_template('login.html', message = msg)
    
    else:
    
        return render_template('login.html')
        
########### LOGOUT PAGE ###########
    
@app.route("/logout")
def logout():
    
    if session.get('userID') is None:
        return redirect(url_for('login'))
    
    for key in session.keys():
     session.pop(key)
     
    return redirect(url_for('main'))
        

########### SIGN UP PAGE ###########

@app.route("/signup", methods=['POST', 'GET'])
def signup():
    
    if session.get('userID'):
        return redirect(url_for('home'))
    
    if request.method == "POST":
    
        username = request.form['username']
        password = request.form['password']
        password2 = request.form['repeat_password']
        
        if Database().get_user_id(username):
            
            error = "Username is taken, please try another!"
            return render_template('signup.html', message = error)
            
        if password != password2:
            
            error = "Please check that your passwords match!"
            return render_template('signup.html', message = error)
        
        if Database().add_user(username, password):
            
            session['user'] = username
            return redirect(url_for('home'))
            
        else:
        
            return redirect('/signup')
            
    else:
    
        return render_template('signup.html')
        
########### RECIPE PAGES ###########

@app.route("/addrecipe", methods=['POST', 'GET'])
def addrecipe():
    
    if session.get('userID') is None:
        return redirect(url_for('login'))
    
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
    

@app.route("/recipes")
def recipes():
    
    if session.get('userID') is None:
        return redirect(url_for('login'))
        
    if request.args.get('sort'):
        order = request.args.get('sort')
    else:
        order = ''
          
    if request.args.get('ingredientID'):
        
        recipes = Database().list_recipes_by_ingredient(request.args.get('ingredientID'), order)
    else:
        recipes = Database().list_recipes(order)
        
    commonIngredients = Database().get_common_ingredients()
    
    return render_template('recipes.html', recipes = recipes, commonIngredients = commonIngredients, uname = session['user'], userID = session['userID'])
    
@app.route("/recipedatabase")
def recipedatabse():
    
    if session.get('userID') is None:
        return redirect(url_for('login'))
        
    if request.args.get('sort'):
        order = request.args.get('sort')
    else:
        order = ''
        
    recipes = Database().list_recipes(order)
    categories = Database().get_categories()
    allIngredients = Database().get_ingredients()
    commonIngredients = Database().get_common_ingredients()
    
    recipes = json.dumps(recipes, indent=4, sort_keys=True, default=str)
    commonIngredients = json.dumps(commonIngredients, indent=4, sort_keys=True, default=str)
    
    return render_template('recipedatabase.html', recipes = recipes, commonIngredients = commonIngredients, categories = categories, allIngredients = allIngredients, uname = session['user'], userID = session['userID'])
    
@app.route("/recipe")
def recipe():
    
    if session.get('userID') is None:
        return redirect(url_for('login'))
    
    recipeID = request.args.get('recipeID')    
    recipe = Database().get_recipe(recipeID)
    recipeIngredients = Database().get_ingredients_for_recipe(recipeID)
    
    userID = session['userID']
    
    Database().add_view(recipeID)
    
    return render_template('recipe.html', recipe = recipe, ingredients = recipeIngredients, userID = userID)
    
@app.route("/editrecipe", methods=['POST', 'GET'])
def editrecipe():
    
    if session.get('userID') is None:
        return redirect(url_for('login'))
    
    recipeID = request.args.get('recipeID')
    categories = Database().get_categories()
    recipe = Database().get_recipe(recipeID)
    ingredients = Database().get_ingredients()
    recipeIngredients = Database().get_ingredients_for_recipe(recipeID)
    
    if request.method == "POST":
    
        recipeID = request.args.get('recipeID')
        title = request.form['title']
        category = request.form['category']
        serves = request.form['serves']
        description = request.form['description']
        
        numIngredients = request.form['ingredientsCount']
        ingredientsDict = {}
        
        if numIngredients:
            for i in range(1, int(numIngredients)+1):
    
                ingName = "newIngredient" + str(i)
                ingQuanName = "newIQ" + str(i)
                
                if ingName in request.form:
                    ingredientID = request.form[ingName]
                    ingredientQuantity = request.form[ingQuanName]
    
                    ingredientsDict[ingredientID] = ingredientQuantity
            
        removedIngredients = request.form['removeList'].split(',')
        
        recipeGF = True if request.form.get('recipeGF') else False
        recipeVegan = True if request.form.get('recipeVegan') else False
        
        if Database().edit_recipe(title, category, serves, description, recipeGF, recipeVegan, session['user'], ingredientsDict, removedIngredients, recipeID):
            
            return redirect(url_for('recipes'))
            
        else:
        
            return redirect(url_for('recipes'))
            
    else:
    
        return render_template('editrecipe.html', recipe = recipe, categories = categories, ingredients = ingredients, recipeIngredients = recipeIngredients)
    
    
@app.route("/deleterecipe")
def deleterecipe():
    
    if session.get('userID') is None:
        return redirect(url_for('login'))
    
    recipeID = request.args.get('recipeID')
    Database().delete_recipe(recipeID)
    
    return redirect('/recipes')
    
    
############# INGREDIENTS PAGES ############# 

@app.route("/ingredients")
def ingredients():
    
    if session.get('userID') is None:
        return redirect(url_for('login'))
        
    ingredients = Database().get_ingredients()
    
    return render_template('ingredients.html', ingredients = ingredients, uname = session['user'], userID = session['userID'])
    

@app.route('/addingredient', methods=['POST', 'GET'])
def addingredient():
    
    if request.method == "POST":
    
        ingredient = request.form['ingredient']
        
        if Database().add_ingredient(ingredient):
            
            return json.dumps({'status':'OK'});
            
        else:
        
            return json.dumps({'status':'ERROR'});
            
    else:
        
        return render_template('addingredient.html')
    

############# OTHER PAGES ############# 


@app.route('/addlike', methods=['POST', 'GET'])
def addlike():
    
    if request.method == "POST":
    
        userID = session.get('userID')
        recipeID = request.args.get('recipeID')
        
        if Database().add_like(userID, recipeID):
            
            return json.dumps({'status':'success'})
            
        else:
        
            return abort(400)
            
    else:
        
        return redirect('recipes')
    
@app.route("/about")
def about():
    return render_template('about.html')
    
@app.route("/home")
def home():
    
    if session.get('userID') is None:
        return redirect(url_for('login'))
        
    recipes = Database().get_liked_recipes(session.get('userID'))
    
    return render_template('home.html', recipes = recipes, uname = session['user'], userID = session['userID'])


@app.route("/")
def main():
    
    def db_query():
        database = Database()
        recipes = database.list_recipes('')
        return recipes
    
    results = db_query()
    
    return render_template('index.html', result=results)
  
if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)