from flask_sqlalchemy import SQLAlchemy
import app

class Sales(app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True, unique = True)
    customerId = app.db.Column(app.db.Integer, nullable = False)
    # category = app.db.Column(app.db.String(80), nullable = False)
    # qty = app.db.Column(app.db.Integer, default = 0)
    amount = app.db.Column(app.db.Integer, nullable = False)
    # salesDate = app.db.Column(app.db.DateTime) 
    weekNo = app.db.Column(app.db.Integer, nullable = False)
    points = app.db.Column(app.db.Integer, default = 0)

