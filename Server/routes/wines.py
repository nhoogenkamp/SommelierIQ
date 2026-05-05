from flask import jsonify
from db import get_db_connection

# reference: https://www.youtube.com/watch?v=14HTiBQEQ9M
# added dictorionary = true to read data in client side: https://stackoverflow.com/questions/22769873/python-mysql-connector-dictcursor

def get_tables():
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    cursor.close()
    con.close()
    table_names = [table[0] for table in tables]
    return jsonify({"tables": table_names}), 200

def get_wines():
    con = get_db_connection()
    cursor = con.cursor(dictionary=True)
    cursor.execute("SELECT * FROM wines;")
    wines = cursor.fetchall()
    cursor.close()
    con.close()
    return jsonify(wines), 200