from flask import request, jsonify, session
from db import get_db_connection
import mysql.connector

# reference: https://www.youtube.com/watch?v=14HTiBQEQ9M
# added dictorionary = true to read data in client side: https://stackoverflow.com/questions/22769873/python-mysql-connector-dictcursor
# order changed https://www.w3schools.com/sql/sql_orderby.asp

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
    cursor.execute("""
    SELECT * FROM wines WHERE available = 1
    ORDER BY
        FIELD(
            bottle_type,
            'Glass',
            'Half Bottle',
            'bottle',
            'magnum',
            'Double Magnum',
            'Jeroboam',
            'Imperial',
            'Salmanazar',
            'Melchior'
        ),
        wine_type ASC,
        country ASC,
        price ASC
    """)
    wines = cursor.fetchall()
    cursor.close()
    con.close()
    return jsonify(wines), 200

def get_all_wines():
    
    if not session.get("loggedin"):
        return jsonify({
            "error": "Please login first"
            }), 401
    
    restaurant_id = session["restaurant_id"]
    con = get_db_connection()
    cursor = con.cursor(dictionary=True)
    check_sql = """
    SELECT * FROM wines WHERE restaurant_id = %s
    ORDER BY
        FIELD(
            bottle_type,
            'Glass',
            'Half Bottle',
            'bottle',
            'magnum',
            'Double Magnum',
            'Jeroboam',
            'Imperial',
            'Salmanazar',
            'Melchior'
        ),
        wine_type ASC,
        country ASC,
        price ASC
    """
    check_value= (restaurant_id,)
    try:
        cursor.execute(check_sql,check_value)
        wines = cursor.fetchall()
    
    except mysql.connector.Error as err:
        print("Error:", err)
        con.rollback()

        return jsonify({
            "error": "Could not delete wine from database"
        }), 500  

    finally:  
        cursor.close()
        con.close()
    return jsonify(wines), 200