from flask import session
from msnweb.mongo import db
from msnweb.models import User


class MSN (object):

    def is_loggedin():
        return 'user_id' in session

    def register_user(email, first_name, last_name, password):
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
                    password=password
                )

        return db.collections.insert_one(user.export())
