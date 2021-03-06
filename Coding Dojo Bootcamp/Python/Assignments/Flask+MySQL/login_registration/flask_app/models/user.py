from flask_app.config.mysqlconnection import connectToMySQL
from flask.helpers import flash
import re

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def insert_user(cls,data):
        query = "INSERT INTO users (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s)"
        return connectToMySQL("users_database").query_db(query,data)

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        user_db = connectToMySQL("users_database").query_db(query,data)

        if len(user_db) < 1:
            return False
        return cls(user_db[0])

    @staticmethod
    def validate_user(user):
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        is_valid = True
        if len(user["first_name"]) < 1:
            flash("First name required!")
            is_valid = False
        if len(user["last_name"]) < 1:
            flash("Last name required!")
            is_valid = False
        if not email_regex.match(user["email"]):
            flash("Invalid email address!")
            is_valid = False    
        if len(user["password"]) < 6:
            flash("Password needs to be at least 6 characters!")
            is_valid = False
        if user["password"] != user["confirm_password"]:
            flash("Passwords do not match!")
            is_valid = False

        return is_valid


    @staticmethod
    def validate_login(user):
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        is_valid = True

        if not email_regex.match(user["email"]):
            flash("Invalid email address!")
            is_valid = False

        if len(user["password"]) < 6:
            flash("Password needs to be at least 6 characters!")
            is_valid = False

        return is_valid

