from mongoengine import *
import datetime
from datetime import datetime
from config import *


class Users(db.Document):
    name     = db.StringField(required=True, max_length=50)
    password = db.StringField(required=True, max_length=200)
    address  = db.StringField(required=True, max_length=200)
    email    = db.StringField(required=True, max_length=50)
    status   = db.BooleanField(default=False)
    created_at = db.DateTimeField(datetime.now())
    updated_at = db.DateTimeField(datetime.now())

