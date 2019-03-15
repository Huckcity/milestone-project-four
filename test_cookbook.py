import os
from flask import session
from app import *
from db import *
import unittest

class CookBookTests(unittest.TestCase):

    def setUp(self):
        """ Create a test client"""
        app.config['SECRET_KEY'] = 'SECERETETEETTETE'
        self.app = app.test_client()
        self.app.testing = True 

    def tearDown(self):
        pass
    

    ### PAGES ACCESSIBLE WITHOUT AUTHORISATION ###

    def test_index(self):
        """Test correct page is rendered for HOME page"""
          
        with app.test_client() as client:
            
            result = client.get("/")
            self.assertEqual(result.status_code, 200)
            
    def test_login_page(self):
        """Test correct page is rendered for LOGIN page"""
          
        with app.test_client() as client:
            
            result = client.get("/login")
            self.assertEqual(result.status_code, 200)
            
    def test_register_page(self):
        """Test correct page is rendered for SIGNUP page"""
          
        with app.test_client() as client:
            
            result = client.get("/signup")
            self.assertEqual(result.status_code, 200)

    def test_about_page(self):
        """Test correct page is rendered for ABOUT page"""
          
        with app.test_client() as client:
            
            result = client.get("/about")
            self.assertEqual(result.status_code, 200)


    ### PAGES NOT ACCESSIBLE WITHOUT AUTHORISATION ###
    
    ### Below we will expect to see 302 errors rather than 404 as we are redirecting the user when they do not have required authorisation ###
    
            
    def test_logout_page_while_unauthorised(self):
        """Test correct page is rendered for LOGOUT WHILE UNAUTHORISED"""
          
        with app.test_client() as client:
            
            attempted_result = client.get("/logout")
            expected_result = client.get("/login")
            
            self.assertEqual(attempted_result.status_code, 302) 
            self.assertEqual(expected_result.status_code, 200)

    
    def test_recipes_page_while_unauthorised(self):
        """Test correct page is rendered for RECIPES WHILE UNAUTHORISED"""
          
        with app.test_client() as client:
            
            attempted_result = client.get("/recipes")
            expected_result = client.get("/login")
            
            self.assertEqual(attempted_result.status_code, 302) 
            self.assertEqual(expected_result.status_code, 200)
        
    def test_add_recipe_page_while_unauthorised(self):
        """Test correct page is rendered for ADD RECIPE UNAUTHORISED"""
          
        with app.test_client() as client:
            
            attempted_result = client.get("/addrecipe")
            expected_result = client.get("/login")
            
            self.assertEqual(attempted_result.status_code, 302) 
            self.assertEqual(expected_result.status_code, 200)
            
    def test_edit_recipe_page_while_unauthorised(self):
        """Test correct page is rendered for EDIT RECIPE UNAUTHORISED"""
          
        with app.test_client() as client:
            
            attempted_result = client.get("/editrecipe")
            expected_result = client.get("/login")
            
            self.assertEqual(attempted_result.status_code, 302) 
            self.assertEqual(expected_result.status_code, 200)
            
            
            
    ### TEST CRUD FUNCTIONS ###
    
    def test_signup(self):
        """Test user can register"""
 
        username = "testuser"
        password = "testpassword"
        
        result = Database().add_user(username, password)
        
        self.assertTrue(result)
        
        
    