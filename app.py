from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
from flask_restful import Resource, Api
import json
from flask_marshmallow import Marshmallow

app = Flask(__name__)
db = SQLAlchemy()
ma = Marshmallow(app)
app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db.init_app(app)

@app.get('/')
def index():    
    return "<p>Flask Rewards API</p>"     

with app.app_context():
    import rewards
    app.register_blueprint(rewards.rw)


# app, ma, db = create_app()
# app.run()


# @app.get('/database')
# def database():
#     return str(app.config['DATABASE'])