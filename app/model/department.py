from app  import db
from app.model.office import Office
from datetime import datetime

class Department(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    office_id = db.Column(db.BigInteger, db.ForeignKey(Office.id, ondelete='CASCADE'))
    name = db.Column(db.String(150), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Department {}>'.format(self.name)