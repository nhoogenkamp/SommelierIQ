from flask import request, jsonify
from db import get_db_connection
from routes.validations import validate_availability

def available_wine():
    data = request.get_json()

    # checking erros in validations.py
    errors = validate_availability(data)

    if errors:
        return jsonify({
            "errors": errors
        }), 400

    wine_id = data["wine_id"]
    available = data["available"]


    con = get_db_connection()
    cursor = con.cursor(dictionary=True)
    
    # checking if wine exist
    check_sql = "SELECT * FROM wines WHERE wine_id = %s"
    check_value= (wine_id,)
    
    cursor.execute(check_sql, check_value)

    wine_exists = cursor.fetchone()
    if not wine_exists:
        cursor.close()
        con.close()
        return jsonify({
            "error": "wine id does not exist"
        }), 404
    
    # update wine in wines table
    sql = "UPDATE wines SET available = %s WHERE wine_id = %s" 
    values = (available,wine_id)

    cursor.execute(sql, values)

    con.commit()

    cursor.close()
    con.close()

    return jsonify({
        "message": "Availability is updated"
    }), 200    