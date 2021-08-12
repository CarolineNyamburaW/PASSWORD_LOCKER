#!/usr/bin/env python
from password import User, Credential

def create_new_user(first_name,last_name,password):
    """
    function to create a new user
    """
    new_user = User(first_name,last_name,password)
    return new_user

def save_user(user):
    """
    function to save user
    """
    user.save_user()

def del_user(user):
    """
    function to delete a user
    """
    user.delete_user()
