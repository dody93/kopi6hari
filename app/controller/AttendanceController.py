from datetime import timedelta
from flask import Flask, request, jsonify
from app import response, app, db
from app.model.attendance import Attendance

def index():
    try:
        attendance = Attendance.query.all()
        data = formatarray(attendance)
        return response.success(data, "Success")
    except Exception as e:
        print(e)

def formatarray(datas):
    array = []
    for i in datas:
        array.append(singleobject(i))
    return array

def singleobject(data):
    def timedelta_to_string(td):
        return str(td) if td else None

    data = {
        'id': data.id,
        'employee_id': data.employee_id,
        'shift_id': data.shift_id,
        'date': data.date,
        'clock_in': data.clock_in,
        'clock_out': data.clock_out,
        'scheduled_time_in': data.scheduled_time_in,
        'selfie_photo': data.selfie_photo,
        'location_gps': data.location_gps,
        'event_note': data.event_note,
        'assistance_request': data.assistance_request,
        'status': data.status,
        'created_at': data.created_at,
        'updated_at': data.updated_at
    }
    return data

def detail(id):
    try:
        attendance = Attendance.query.filter_by(id=id).first()
        if not attendance:
            return response.badRequest([], 'Tidak ada Data Shifts')
        
        data = singleDetailAttendance(attendance)
        return response.success(data, "success")
    
    except Exception as e:
        print(e)

def singleDetailAttendance(attendance):
    def timedelta_to_string(td):
        return str(td) if td else None

    data = {
        'id': attendance.id,
        'employee_id': attendance.employee_id,
        'shift_id': attendance.shift_id,
        'date': attendance.date,
        'clock_in': attendance.clock_in,
        'clock_out': attendance.clock_out,
        'scheduled_time_in': attendance.scheduled_time_in,
        'selfie_photo': attendance.selfie_photo,
        'location_gps': attendance.location_gps,
        'event_note': attendance.event_note,
        'assistance_request': attendance.assistance_request,
        'status': attendance.status,
        'created_at': attendance.created_at,
        'updated_at': attendance.updated_at
    }
    return data

def save():
    try:
        employee_id = request.form.get('employee_id')
        shift_id = request.form.get('shift_id')
        date = request.form.get('date')
        clock_in = request.form.get('clock_in')
        clock_out = request.form.get('clock_out')
        scheduled_time_in = request.form.get('scheduled_time_in')
        selfie_photo = request.form.get('selfie_photo')
        location_gps = request.form.get('location_gps')
        event_note = request.form.get('event_note')
        assistance_request = request.form.get('assistance_request')
        status = request.form.get('status')
        created_at = request.form.get('created_at')
        updated_at = request.form.get('updated_at')

        attendance = Attendance(employee_id=employee_id, shift_id=shift_id, date=date, clock_in=clock_in, clock_out=clock_out , scheduled_time_in=scheduled_time_in,
                        selfie_photo=selfie_photo, location_gps=location_gps, event_note=event_note,
                        assistance_request=assistance_request, status=status, created_at=created_at, updated_at=updated_at)
        db.session.add(attendance)
        db.session.commit()

        return response.success('', 'Sukses Menambahkan Data Attendace')
    except Exception as e:
        print(e)

def update(id):
    try:
        employee_id = request.form.get('employee_id')
        shift_id = request.form.get('shift_id')
        date = request.form.get('date')
        clock_in = request.form.get('clock_in')
        clock_out = request.form.get('clock_out')
        scheduled_time_in = request.form.get('scheduled_time_in')
        selfie_photo = request.form.get('selfie_photo')
        location_gps = request.form.get('location_gps')
        event_note = request.form.get('event_note')
        assistance_request = request.form.get('assistance_request')
        status = request.form.get('status')
        created_at = request.form.get('created_at')
        updated_at = request.form.get('updated_at')


        attendance = Attendance.query.filter_by(id=id).first()

        if not attendance:
            return response.error(None, 'Shifts not found'), 404

        if employee_id is not None:
            attendance.employee_id= employee_id
        if shift_id is not None:
            attendance.shift_id = shift_id
        if date is not None:
            attendance.date = date
        if clock_in is not None:
            attendance.clock_in = clock_in
        if clock_out is not None:
            attendance.clock_out = clock_out
        if scheduled_time_in is not None:
            attendance.scheduled_time_in = scheduled_time_in
        if selfie_photo is not None:
            attendance.selfie_photo = selfie_photo
        if location_gps is not None:
            attendance.location_gps = location_gps
        if event_note is not None:
            attendance.event_note = event_note
        if assistance_request is not None:
            attendance.assistance_request = assistance_request
        if status is not None:
            attendance.status = status
        if created_at is not None:
            attendance.created_at = created_at
        if updated_at is not None:
            attendance.updated_at = updated_at

        db.session.commit()

        input_data = singleobject(attendance)
        return response.success(input_data, 'Sukses Update Data')
    except Exception as e:
        print(e)
        return response.error(None, str(e)), 500

def delete(id):
    try:
        attendance = Attendance.query.filter_by(id=id).first()
        if not attendance:
            return response.badRequest([], 'Data Shifts Kosong')
        db.session.delete(attendance)
        db.session.commit()

        return response.success('', 'Berhasil Menghapus Data')
    except Exception as e:
        print(e)
