from app.model.users import Users

from app import response, app, db
from flask import request

def index():
    try:
        users = Users.query.all()
        data = formatarray(users)
        return response.success(data, "Success")
    except Exception as e :
        print(e)


def formatarray(datas):
    array = []

    for i in datas:
        array.append(singleobject(i))

    return array

def singleobject(data):
    data = {
        'id' : data.id,
        'username' : data.username,
        'email' : data.email,
        'email_verified_at' : data.email_verified_at,
        'password' : data.password,
        'remember_token' : data.remember_token,
        'is_active' : data.is_active,
        'created_at' : data.created_at,
        'updated_at' : data.updated_at
    }

    return data

def detail(id):
    try:
        users = Users.query.filter_by(id=id).first()

        if not users:
            return response.badRequest([],'Tidak ada Data Users')
        
        data = singleDetailUsers(users)

        return response.success(data, "success")
    
    except Exception as e :
        print(e)
    
def singleDetailUsers(users):
    data = {
        'id' : users.id,
        'username' : users.username,
        'email' : users.email,
        'email_verified_at' : users.email_verified_at,
        'password' : users.password,
        'remember_token' : users.remember_token,
        'is_active' : users.is_active,
        'created_at' : users.created_at,
        'updated_at' : users.updated_at
    }

    return data

    
#insert Data

def save():
    try:
        username = request.form.get('username')
        email = request.form.get('email')
        email_verified_at = request.form.get('email_verified_at')
        password = request.form.get('password')
        remember_token = request.form.get('remember_token')
        is_active = request.form.get('is_active')
        created_at = request.form.get('created_at')
        updated_at = request.form.get('updated_at')

        users = Users(username=username, email=email, email_verified_at=email_verified_at, password=password, remember_token=remember_token, is_active=is_active, created_at=created_at, updated_at=updated_at)
        db.session.add(users)
        db.session.commit()

        return response.success('','Sukses Menambahkan Data Users')
    except Exception as e:
        print(e)


#Update Data

def update(id):
    try:
        username = request.form.get('username')
        email = request.form.get('email')
        email_verified_at = request.form.get('email_verified_at')
        password = request.form.get('password')
        remember_token = request.form.get('remember_token')
        is_active_str = request.form.get('is_active')
        created_at = request.form.get('created_at')
        updated_at = request.form.get('updated_at')

        # Konversi is_active ke boolean
        if is_active_str is not None:
            if is_active_str.lower() == 'true':
                is_active = True
            elif is_active_str.lower() == 'false':
                is_active = False
            else:
                return response.error(None, 'Invalid value for is_active'), 400
        else:
            is_active = None  # Atur sesuai kebutuhan jika nilai is_active tidak disediakan

        input_data = {
            'username': username,
            'email': email,
            'email_verified_at': email_verified_at,
            'password': password,
            'remember_token': remember_token,
            'is_active': is_active,
            'created_at': created_at,
            'updated_at': updated_at
        }

        user = Users.query.filter_by(id=id).first()

        if not user:
            return response.error(None, 'User not found'), 404

        # Perbarui hanya jika nilai yang diberikan tidak None
        if username is not None:
            user.username = username
        if email is not None:
            user.email = email
        if email_verified_at is not None:
            user.email_verified_at = email_verified_at
        if password is not None:
            user.password = password
        if remember_token is not None:
            user.remember_token = remember_token
        if is_active is not None:
            user.is_active = is_active
        if created_at is not None:
            user.created_at = created_at
        if updated_at is not None:
            user.updated_at = updated_at

        db.session.commit()

        return response.success(input_data, 'Sukses Update Data')
    except Exception as e:
        print(e)
        return response.error(None, str(e)), 500


#Delete Data

def delete(id):
    try:
        users = Users.query.filter_by(id=id).first()
        if not users:
            return response.badRequest([], 'Data Users Kosong')
        db.session.delete(users)
        db.session.commit()

        return response.success('', 'Berhasil Menghapus Data')
    except Exception as e:
        print(e)
