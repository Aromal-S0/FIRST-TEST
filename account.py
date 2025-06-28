# account.py

from database import users_db

def deposit(username, amount):
    if amount > 0:
        users_db[username]['balance'] += amount
        return True
    return False

def withdraw(username, amount):
    if 0 < amount <= users_db[username]['balance']:
        users_db[username]['balance'] -= amount
        return True
    return False

def get_balance(username):
    return users_db[username]['balance']
