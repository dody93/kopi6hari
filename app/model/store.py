from app  import db
from app.model.branch import Branch
from datetime import datetime

class Store(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    store_id = db.Column(db.BigInteger, db.ForeignKey(Branch.id, ondelete='CASCADE'))
    code = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    address = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Store {}>'.format(self.name)