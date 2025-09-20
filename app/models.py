from datetime import datetime
from .extensions import db

class user(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,
                   primary_key=True)
    email = db.Column(db.String(120), 
                      unique=True, 
                      nullable=False,
                      index=True)
    password = db.Column(db.String(255),
                         nullable=False)
    created_at = db.Column(db.DateTime,
                           default=datetime.utcnow())