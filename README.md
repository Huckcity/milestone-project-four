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
- Flask
- HTML
- CSS
- MaterializeCSS
- JQuery
    - [Pagination.js](https://pagination.js.org/)
    - [List.js](https://listjs.com/)

## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X
