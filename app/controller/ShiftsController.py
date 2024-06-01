from datetime import timedelta
from flask import Flask, request, jsonify
from app import response, app, db
from app.model.shifts import Shifts

def index():
    try:
        shifts = Shifts.query.all()
        data = formatarray(shifts)
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
        'name': data.name,
        'start_time': data.start_time,
        'end_time': data.end_time,
        'break_out': timedelta_to_string(data.break_out),
        'break_in': timedelta_to_string(data.break_in),
        'overtime_before': timedelta_to_string(data.overtime_before),
        'overtime_after': timedelta_to_string(data.overtime_after),
        'is_default': data.is_default,
        'created_at': data.created_at,
        'updated_at': data.updated_at
    }
    return data

def detail(id):
    try:
        shifts = Shifts.query.filter_by(id=id).first()
        if not shifts:
            return response.badRequest([], 'Tidak ada Data Shifts')
        
        data = singleDetailShifts(shifts)
        return response.success(data, "success")
    
    except Exception as e:
        print(e)

def singleDetailShifts(shifts):
    def timedelta_to_string(td):
        return str(td) if td else None

    data = {
        'id': shifts.id,
        'name': shifts.name,
        'start_time': shifts.start_time,
        'end_time': shifts.end_time,
        'break_out': timedelta_to_string(shifts.break_out),
        'break_in': timedelta_to_string(shifts.break_in),
        'overtime_before': timedelta_to_string(shifts.overtime_before),
        'overtime_after': timedelta_to_string(shifts.overtime_after),
        'is_default': shifts.is_default,
        'created_at': shifts.created_at,
        'updated_at': shifts.updated_at
    }
    return data

def save():
    try:
        name = request.form.get('name')
        start_time = request.form.get('start_time')
        end_time = request.form.get('end_time')
        break_out = request.form.get('break_out')
        break_in = request.form.get('break_in')
        overtime_before = request.form.get('overtime_before')
        overtime_after = request.form.get('overtime_after')
        is_default = request.form.get('is_default')
        created_at = request.form.get('created_at')
        updated_at = request.form.get('updated_at')

        shifts = Shifts(name=name, start_time=start_time, end_time=end_time, break_out=break_out, break_in=break_in,
                        overtime_before=overtime_before, overtime_after=overtime_after, is_default=is_default,
                        created_at=created_at, updated_at=updated_at)
        db.session.add(shifts)
        db.session.commit()

        return response.success('', 'Sukses Menambahkan Data Shifts')
    except Exception as e:
        print(e)

def update(id):
    try:
        name = request.form.get('name')
        start_time = request.form.get('start_time')
        end_time = request.form.get('end_time')
        break_out = request.form.get('break_out')
        break_in = request.form.get('break_in')
        overtime_before = request.form.get('overtime_before')
        overtime_after = request.form.get('overtime_after')
        is_default = request.form.get('is_default')
        created_at = request.form.get('created_at')
        updated_at = request.form.get('updated_at')

        shifts = Shifts.query.filter_by(id=id).first()

        if not shifts:
            return response.error(None, 'Shifts not found'), 404

        if name is not None:
            shifts.name = name
        if start_time is not None:
            shifts.start_time = start_time
        if end_time is not None:
            shifts.end_time = end_time
        if break_out is not None:
            shifts.break_out = break_out
        if break_in is not None:
            shifts.break_in = break_in
        if overtime_before is not None:
            shifts.overtime_before = overtime_before
        if overtime_after is not None:
            shifts.overtime_after = overtime_after
        if is_default is not None:
            shifts.is_default = is_default
        if created_at is not None:
            shifts.created_at = created_at
        if updated_at is not None:
            shifts.updated_at = updated_at

        db.session.commit()

        input_data = singleobject(shifts)
        return response.success(input_data, 'Sukses Update Data')
    except Exception as e:
        print(e)
        return response.error(None, str(e)), 500

def delete(id):
    try:
        shifts = Shifts.query.filter_by(id=id).first()
        if not shifts:
            return response.badRequest([], 'Data Shifts Kosong')
        db.session.delete(shifts)
        db.session.commit()

        return response.success('', 'Berhasil Menghapus Data')
    except Exception as e:
        print(e)
