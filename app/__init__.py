from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app.model import user, dosen, mahasiswa, users, office, branch, store, department, roles, positions, employee, employee_roles, shifts, attendance, employee_personal_information,employee_emergency_contacts, employee_families
from app import routes
