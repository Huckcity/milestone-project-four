# Cookbook Recipe Website

Cookbook is a site designed to help you improve your culinary skills and repertoire. Browse through our recipes for something new, or if you have an exciting idea 
to share post it here for everyone else to try! Hit the like button on any recipes you want to bookmark and we'll keep them on your home page for later. Bon Appetit!
 
## UX

This website it designed for the average casual web user, and is designed to be as intuitive and simple to follow as possible. It is intended for casual users to be able to join the site, view existing recipes and add their own recipes to the site.
To enable the user to achieve these goals we have designed each page to be intuitive, and require a minimal amount of navigation and page loads to achieve their goals.

<br>

- As an unauthorised user, I want to be able to view the home page
- As an unauthorised user, I want to be able to view the login page
- As an unauthorised user, I want to be able to view the signup page
- As an unauthorised user, I want to be able to view the about page

<br>

- As an authorised user, I want to be able to view the user home page
- As an authorised user, I want to be able to view the recipes page
- As an authorised user, I want to be able to view the add recipe page
- As an authorised user, I want to be able to view the edit recipe page
- As an authorised user, I want to be able to add a recipe
- As an authorised user, I want to be able to edit a recipe
- As an authorised user, I want to be able to delete a recipe
- As an authorised user, I want to be able to like a recipe

All of the above user stories can be completed with a maximum of two page loads, in keeping with out UX design goals.

###wireframes here

## Features

**Home** - Static landing page
<br>
<br>
**Login** - The user is able to enter their username and password to log in. If the details are incorrect the user is returned to the login page and notified of the error.
<br>
<br>
**Signup** - The user is able to enter a username and password to create an account. If the username is taken or the passwords don't match, the user is redirected to the signup page and notified of the error.
<br>
<br>
**Logout** - The user is logged out of the current session and returned to the front page
<br>
<br>
**Recipes** - The user is presented with a comprehensive, paginated list of all current recipes. There is a responsive search feature to quickly find a specific recipe, or all recipes containing a specific word e.g. find all recipes containing the word 'chicken'. 
                The recipes list can be sorted by number or views or number of likes, ascending or descending. There is also a common ingredients section to allow the user to view recipes based on some of the most common ingredients, which will encourage the user
                to discover recipes they may not have previously considered. Each listed recipe can be viewed, edited or deleted from this section also.
<br>
<br>
**View Recipe** - The user is presented with a summary of the selected recipe, including all relevant details. If there are missing ingredients the user is prompted to add some. The user can also go on to like, edit or delete the recipe.
<br>
<br>
**Add Recipe** - The user is presented with a form to add a new recipe. The form is standard is most ways, other than the add ingredients section. This section is designed to provide immediate feedback to the user while adding ingredients, and allows for removal of ingredients prior to commiting any details to the databse. 
<br>
<br>
**Edit Recipe** - The user is presented with a pre-populated form, which is modeled after the add recipe form and pre-populated with any existing data. The user can also cancel this process safely.
<br>
<br>
**Delete Recipe** - The user is prompted to confirm deletion of the recipe and can cancel in case of error.
<br>
<br>
**Ingredients** - The user is presented with a comprehensive list of ingredients, which is searchable in the same manner as the recipes page. If the user searches for an ingredient and does not find it, they can simply click to add the ingredient to the database.
<br>
<br>
**Recipe Database** - The database page provides statistical information for all recipes in the database. 
<br>
<br>


### Features Left to Implement
- I would like to implement several other metrics on the recipes, such as cooking time, coutry of origin etc. but chose to exclude these as they would not demonstrate any additional developmental skillsets
- With extra metrics a more comprehensive search feature would be a necessary feature to implement also
- Allowing users to add their own images for recipes

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- Python
- MySQL
- Flask
- HTML
- CSS
- MaterializeCSS
- JQuery
    - [Pagination.js](https://pagination.js.org/)
    - [List.js](https://listjs.com/)

- Heroku Hosting Platform
    - ClearDB MySQL Add-On


## Testing

In this project I have strived to automate testing as much as possible. Unit testing can be found in [test_cookbook.py](https://github.com/Huckcity/milestone-project-four/blob/master/test_cookbook.py). To run the tests simply perform ```python3 test_cookbook.py```
These tests ensure all pages and templates are rendered as expected based on whether the user is logged in/out, and also tests CRUD functionality for the recipes database. Unfortunately, having chosen MySQL as the database solution for this project, I discovered the difficulty in testing against a mock database when compared with SQLite or NoSQL options. As such, all tests run against the live database. One solution to this would be to create a second database entirely for testing, but this was discovered towards the end of development and has been left out for submission.

As per the above <b>user stories</b>, I also manually tested each use case to ensure the correct behavior, for exmaple:

- Signup Page
    1. Try to submit the form with no details provided and ensure the correct error message was displayed.
    2. Try to submit the form with correct data and ensure the page submitted correctly
    3. Try to submit the form with mismatched passwords and ensure the correct error message was displayed

This process was carried out for each use case successfully.

In terms of browser compatibility and display, I am relatively happy with the sites performance across multiple devices. There are certain design choices that could be reconsidered, but with the exception of the Recipe Database page the site is functional in all test cases:
- Desktop 24" 1920x1080 display
- Macbook Pro 15"
- iPad 4 9.7"
- Xiaomi Air 13" (Ubuntu)
- Honor Play 6.3"

## Deployment

This application is source controlled via GIT at https://github.com/Huckcity/milestone-project-four
It has been deployed to Heroku for demonstration purposes at https://milestone-project-four.herokuapp.com/

To deploy to Heroku, we had to generate a Procfile to allow Heroku to identify the type of application it was handling, and we have our required libraries exported to a requirements.txt file to allow all dependencies to be installed automatically by the host.
To deploy locally, take the follow steps:
- Download source code, open terminal in source folder
- ```pip install -r requirements.txt```
- ```python app.py```
- Open ```http://127.0.0.1:5000```


## Credits

### Content
- The recipe content was loosely pulled from [recipes.com](http://www.recipes.com) and then further populated the database with dummy content

### Media

- The photos used were taken from Google images