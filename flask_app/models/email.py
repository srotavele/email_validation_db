from ..config.mysqlconnections import connectToMySQL
from flask import flash
import re


class User:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        results = connectToMySQL('valid_email_schema').query_db(query)
        
        emails = []
        
        for row in results:
            emails.append(User(row))
        return emails
    
    
    @staticmethod
    def validate_address(post_data):
        is_valid = True
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            flash("Email address is not valid.")
            is_valid = False
        
        return is_valid
    
    
    @classmethod
    def add_email(cls,data):
        query = "INSERT INTO users (email, created_at, updated_at) VALUES (%(email)s, NOW(),NOW());"
        results = connectToMySQL('valid_email_schema').query_db(query,data)
        
        return results
    
    @classmethod 
    def get_entry(cls):
        query = "SELECT * FROM users ORDER BY id DESC;"
        results = connectToMySQL('valid_email_schema').query_db(query)
        return results
    
    @classmethod
    def delete_entry(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        results = connectToMySQL('valid_email_schema').query_db(query,data)
        return results