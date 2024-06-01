from app import app
from app.controller import UsersController
from app.controller import ShiftsController
from app.controller import AttendanceController
from flask import request


@app.route('/')
def index():
    return 'Hello Flask App'

    
@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        return UsersController.index()
    else:
        return UsersController.save()

@app.route('/users/<id>', methods=['GET','PUT','DELETE'])
def usersDetail(id):
    if request.method == 'GET':
        return UsersController.detail(id)
    elif request.method == 'PUT':
        return UsersController.update(id)
    elif request.method == 'DELETE':
        return UsersController.delete(id)
    

@app.route('/shifts', methods=['GET', 'POST'])
def shifts():
    if request.method == 'GET':
        return ShiftsController.index()
    else:
        return ShiftsController.save()

@app.route('/shifts/<id>', methods=['GET','PUT','DELETE'])
def shiftsDetail(id):
    if request.method == 'GET':
        return ShiftsController.detail(id)
    elif request.method == 'PUT':
        return ShiftsController.update(id)
    elif request.method == 'DELETE':
        return ShiftsController.delete(id)


@app.route('/attendance', methods=['GET', 'POST'])
def attendance():
    if request.method == 'GET':
        return AttendanceController.index()
    else:
        return AttendanceController.save()

@app.route('/attendance/<id>', methods=['GET','PUT','DELETE'])
def attendanceDetail(id):
    if request.method == 'GET':
        return AttendanceController.detail(id)
    elif request.method == 'PUT':
        return AttendanceController.update(id)
    elif request.method == 'DELETE':
        return AttendanceController.delete(id)
