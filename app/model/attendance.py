from app  import db
from app.model.employee import Employee
from app.model.shifts import Shifts
from datetime import datetime

class Attendance(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    employee_id = db.Column(db.BigInteger, db.ForeignKey(Employee.id, ondelete='CASCADE'))
    shift_id = db.Column(db.BigInteger, db.ForeignKey(Shifts.id, ondelete='CASCADE'))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    clock_in = db.Column(db.DateTime, default=datetime.utcnow)
    clock_out = db.Column(db.DateTime, default=datetime.utcnow)
    scheduled_time_in = db.Column(db.DateTime, default=datetime.utcnow)
    selfie_photo = db.Column(db.String(250), nullable=False)
    location_gps = db.Column(db.String(250), nullable=False)
    event_note = db.Column(db.Text, nullable=False)
    assistance_request = db.Column(db.Boolean, default=True)
    status = db.Column(db.SmallInteger, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Attendance {}>'.format(self.name)