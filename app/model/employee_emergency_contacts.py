from app  import db
from app.model.employee import Employee
from datetime import datetime

class Employee_Emergency_Contacts(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    employee_id = db.Column(db.BigInteger, db.ForeignKey(Employee.id, ondelete='CASCADE'))
    name = db.Column(db.String(100), nullable=False)
    relationship = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Employee_Emergency_Contacts {}>'.format(self.name)