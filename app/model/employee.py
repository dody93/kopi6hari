from app  import db
from app.model.users import Users
from app.model.office import Office
from app.model.branch import Branch
from app.model.store import Store
from app.model.department import Department
from app.model.positions import Positions
from datetime import datetime

class Employee(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey(Users.id, ondelete='CASCADE'))
    office_id = db.Column(db.BigInteger, db.ForeignKey(Office.id, ondelete='CASCADE'))
    branch_id = db.Column(db.BigInteger, db.ForeignKey(Branch.id, ondelete='CASCADE'))
    store_id = db.Column(db.BigInteger, db.ForeignKey(Store.id, ondelete='CASCADE'))
    department_id = db.Column(db.BigInteger, db.ForeignKey(Department.id, ondelete='CASCADE'))
    position_id = db.Column(db.BigInteger, db.ForeignKey(Positions.id, ondelete='CASCADE'))
    employee_code = db.Column(db.String(250), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    employee_status = db.Column(db.SmallInteger, nullable=False)
    email = db.Column(db.String(50), index=True, unique=True, nullable=False)
    join_date = db.Column(db.DateTime, default=datetime.utcnow)
    end_status_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Employee {}>'.format(self.name)