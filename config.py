from flask import Flask
from flask_mongoengine import MongoEngine

#db = MongoEngine()

app=Flask(__name__)
db = MongoEngine(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/learn"
db.init_app(app)

