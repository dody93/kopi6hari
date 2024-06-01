from app  import db
from datetime import datetime

class Users(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    username = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(50), index=True, unique=True, nullable=False)
    email_verified_at = db.Column(db.DateTime, default=datetime.utcnow)
    password = db.Column(db.String(250), nullable=False)
    remember_token = db.Column(db.String(250), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Users {}>'.format(self.name)