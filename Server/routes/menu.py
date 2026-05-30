from flask import jsonify
from db import get_db_connection
import mysql.connector

def get_food():
    # 503 error for connection
    try:
        con = get_db_connection()
        cursor = con.cursor(dictionary=True)

    except mysql.connector.Error as err:
        print("Error:", err.errno)

        return jsonify({
            "error": "Could not connect with database"
        }), 503   

    try:
        cursor.execute("SELECT * FROM food_items;")
        foods = cursor.fetchall()
    except mysql.connector.Error as err:
        print("Error:", err)

        return jsonify({
            "error": "Could not get food items from database"
        }), 500
    
    finally:
        cursor.close()
        con.close()
    return jsonify(foods), 200