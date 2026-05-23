from flask import request, jsonify
from db import get_db_connection

def delete_wine():
    data = request.get_json()
    print(data)

    wine_id = data["wine_id"]

    con = get_db_connection()
    cursor = con.cursor(dictionary=True)
   
    # insert admin into admins table
    sql = "DELETE FROM wines WHERE wine_id = %s"
    values = (wine_id,)

    cursor.execute(sql, values)

    con.commit()

    cursor.close()
    con.close()

    return jsonify({
        "message": "Wine is deleted"
    }), 200   