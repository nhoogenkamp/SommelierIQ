from flask import request, jsonify
from db import get_db_connection
# flask library that helps create and read passwords
from werkzeug.security import generate_password_hash, check_password_hash

def add_admin():

    # get JSON data sent from JavaScript
    data = request.get_json()

    print(data)

    restaurant_id = data["restaurant_id"]
    username = data["username"]
    password = data["password"]

    # turn normal password into hashed password
    password_hash = generate_password_hash(password)

    con = get_db_connection()
    cursor = con.cursor(dictionary=True)

    # checking if user exist
    check_sql = "SELECT * FROM admins WHERE username = %s"
    check_value= (username,)
    
    cursor.execute(check_sql, check_value)

    admin_exists = cursor.fetchone()
    if admin_exists:
        cursor.close()
        con.close()
        return jsonify({
            "error": "Username already exists"
        }), 400

    # insert admin into admins table
    sql = "INSERT INTO admins (restaurant_id, username, password_hash) VALUES (%s, %s, %s)"
    values = (restaurant_id, username, password_hash)

    cursor.execute(sql, values)

    con.commit()

    cursor.close()
    con.close()

    return jsonify({
        "message": "Admin account created"
    }), 200

def login_admin():

    data = request.get_json()
    print(data)

    username = data["username"]
    password = data["password"]

    con = get_db_connection()
    cursor = con.cursor(dictionary=True)

    sql = "SELECT * FROM admins WHERE username = %s"
    values = (username,)

    cursor.execute(sql, values)

    admin = cursor.fetchone()

    cursor.close()
    con.close()

    # check if admin exists and password matches hashed password: https://medium.com/%40premnathm/implementing-login-functionality-in-a-flask-application-64929c6f146e#:~:text=if%20hashed_password%20and%20check_password_hash(hashed_password%5B0%5D%2C%20password)%3A%20%23%20Verify%20the%20password%20using%20check_password_hash%0Asession%5B%E2%80%98username%E2%80%99%5D%20%3D%20username%20%23%20Start%20a%20user%20session%0Aflash(%E2%80%98You%20were%20successfully%20logged%20in%E2%80%99)%0Areturn%20redirect(url_for(%E2%80%98index%E2%80%99))
    if admin and check_password_hash(admin["password_hash"], password):

        return jsonify({
            "message": "Login successful",
            "username": admin["username"]
        }), 200

    return jsonify({
        "error": "Incorrect username or password"
    }), 401