from flask import jsonify
from db import get_db_connection

def get_food():
    con = get_db_connection()
    cursor = con.cursor(dictionary=True)
    cursor.execute("SELECT * FROM food_items;")
    foods = cursor.fetchall()
    cursor.close()
    con.close()
    return jsonify(foods), 200