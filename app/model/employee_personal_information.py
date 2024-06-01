from app  import db
from app.model.employee import Employee
from datetime import datetime

class Employee_Personal_Information(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    employee_id = db.Column(db.BigInteger, db.ForeignKey(Employee.id, ondelete='CASCADE'))
    mobile_phone = db.Column(db.Integer, nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    place_of_birth = db.Column(db.String(100), nullable=False)
    birthdate = db.Column(db.DateTime, default=datetime.utcnow)
    gender = db.Column(db.SmallInteger, nullable=False)
    marital_status = db.Column(db.SmallInteger, nullable=False)
    blood_type = db.Column(db.SmallInteger, nullable=False)
    religion = db.Column(db.SmallInteger, nullable=False)
    identity_type = db.Column(db.SmallInteger, nullable=False)
    identity_number = db.Column(db.Integer, nullable=False)
    identity_expiry_date = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Employee_Personal_Information {}>'.format(self.name)