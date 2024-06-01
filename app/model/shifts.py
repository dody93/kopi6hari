from app  import db
from datetime import datetime

class Shifts(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), nullable=False)
    start_time = db.Column(db.DateTime, default=datetime.utcnow)
    end_time = db.Column(db.DateTime, default=datetime.utcnow)
    break_out = db.Column(db.DateTime, default=datetime.utcnow)
    break_in = db.Column(db.DateTime, default=datetime.utcnow)
    overtime_before = db.Column(db.DateTime, default=datetime.utcnow)
    overtime_after = db.Column(db.DateTime, default=datetime.utcnow)
    is_default = db.Column(db.SmallInteger, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Shifts {}>'.format(self.name)