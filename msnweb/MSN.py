from flask import session
from msnweb.mongo import db
from msnweb.models import User
from bson.objectid import ObjectId


class MSN (object):

    def is_loggedin():
        return 'user_id' in session

    def register_user(email, first_name, last_name, password, bio=''):
        existing_user = db.collections.find_one({
            'email': email,
            'structure': '#User'
            })
        
        if existing_user is not None:
            return False

        user = User(
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=password,
                    bio=bio
                )

        return db.collections.insert_one(user.export())

    def login(email, password):
        existing_user = db.collections.find_one({
            'email': email,
            'structure': '#User'
            })

        if existing_user is None:
            return False

        if existing_user['password'] == password:
            session['user_id'] = str(existing_user['_id'])
            return True

    def get_all_users():
        users = list(db.collections.find({
                'structure': '#User'
            }))

        return users
    
    def get_current_user():
        if not MSN.is_loggedin():
            return None

        current_user = db.collections.find_one({
                'structure': '#User',
                '_id': ObjectId(session['user_id'])
            })

        return current_user
