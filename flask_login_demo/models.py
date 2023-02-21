
from sqlalchemy import Column, String, Integer, Text,create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


db = SQLAlchemy()

def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@0.0.0.0:5432/Rocket"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    db.app = app
    db.init_app(app)
    db.create_all()

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False, unique=True)
    password = Column(String(250), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
