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

def find_user(password):
    """
    function that finds a user by password and returns the user
    """
    return User.find_user_by_password(password)

def display_user():
    """
    function to display user
    """
    return User.display_user()




def create_new_credential(Account,username,password):
    """
    function that creates new credential for a given user account
    """

    new_credential = Credential(Account,username,password)
    return new_credential

def save_credential(credential):
    """
    function to save credential 
    """

    credential.save_credential()

def delete_credential(credential):
    """
    function to delete a credential
    """
    credential.delete_credential()

def find_credential(username):
    """
    function that finds a user by password and returns the credential
    """
    return Credential.find_credential(username)

def display_credential():
    """
    function that finds a credential
    """
    return Credential.display_credential()    

def credential_exists(account):
    """
    Function that check if a Credentials exists with that account name and return true or false
    """
    return Credential.if_credential_exists(account)