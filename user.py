# user.py

from database import users_db

def create_user(username, password):
    if username in users_db:
        return False
    users_db[username] = {'password': password, 'balance': 0}
    return True

def authenticate_user(username, password):
    user = users_db.get(username)
    if user and user['password'] == password:
        return True
    return False
