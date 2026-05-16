from flask import request, jsonify
from db import get_db_connection
# flask library that helps create and read passwords
from werkzeug.security import generate_password_hash

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