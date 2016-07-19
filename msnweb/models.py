import time
import json


class DBObject(object):
    """This class defines how objects in the mongoDB should be represented."""

    def __init__(
            self,
            classes=[],
            type='',
            meta={}
            ):
        self.created = time.strftime("%Y/%B/%d|%H:%M:%S")
        self.updated = time.strftime("%Y/%B/%d|%H:%M:%S")
        self.classes = classes
        self.type = type
        self.meta = meta
        self.structure = '{}{}'.format('#', self.__class__.__name__)


    def export(self):
        """This function exports the object as a dict. This is used when
        putting an object in the database."""

        return self.__dict__

class User(DBObject):

    def __init__(
            self,
            email='',
            first_name='',
            last_name='',
            password='',
            role='user',
            avatar=None,
            bio='',
            *args,
            **kwargs
            ):
        DBObject.__init__(self, *args, **kwargs)
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.role = role
        self.avatar = avatar
        self.bio = bio

class Conversation(DBObject):

    def __init__(
            self,
            title='',
            user_ids=[],
            ver=0,
            *args,
            **kwargs
            ):
        DBObject.__init__(self, *args, **kwargs)
        self.title = title
        self.user_ids = user_ids
        self.ver = ver

class Message(DBObject):

    def __init__(
            self,
            conversation_id=None,
            body='',
            sender_id=None,
            *args,
            **kwargs
            ):
        DBObject.__init__(self, *args, **kwargs)
        self.conversation_id = conversation_id
        self.sender_id = sender_id
        self.body = body
