from app  import db
from app.model.employee import Employee
from datetime import datetime

class Employee_Families(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    employee_id = db.Column(db.BigInteger, db.ForeignKey(Employee.id, ondelete='CASCADE'))
    fullname = db.Column(db.String(100), nullable=False)
    relationship = db.Column(db.String(100), nullable=False)
    address = db.Column(db.Text, nullable=False)
    id_number = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.SmallInteger, nullable=False)
    birthdate = db.Column(db.DateTime, default=datetime.utcnow)
    religion = db.Column(db.SmallInteger, nullable=False)
    marital_status = db.Column(db.SmallInteger, nullable=False)
    job = db.Column(db.SmallInteger, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Employee_Families {}>'.format(self.name)