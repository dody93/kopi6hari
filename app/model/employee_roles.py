from app  import db
from app.model.employee import Employee
from app.model.roles import Roles
from datetime import datetime

class Employee_Roles(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    employee_id = db.Column(db.BigInteger, db.ForeignKey(Employee.id, ondelete='CASCADE'))
    role_id = db.Column(db.BigInteger, db.ForeignKey(Roles.id, ondelete='CASCADE'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Employee_Roles {}>'.format(self.name)