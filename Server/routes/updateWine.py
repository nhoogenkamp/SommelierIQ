from flask import request, jsonify
from db import get_db_connection

def update_wine():
    data = request.get_json()
    print(data)

    wine_id = data["wine_id"]
    price = data["price"]


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
    sql = "UPDATE wines SET price = %s WHERE wine_id = %s" 
    values = (price,wine_id)

    cursor.execute(sql, values)

    con.commit()

    cursor.close()
    con.close()

    return jsonify({
        "message": "Price is updated"
    }), 200    