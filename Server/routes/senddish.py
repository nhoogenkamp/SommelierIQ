from flask import request, jsonify
from db import get_db_connection

# Function handles POST request from frontend
def send_dish():

    # Reading the JSON sent
    data = request.get_json()
    # Print received data in Flask terminal
    print(data)

    # Get the value stored in the key "dish"
    selected_dish = data["dish"]

    con = get_db_connection()
    cursor = con.cursor(dictionary=True)

    # SQL query searches for matching food item : https://www.w3schools.com/python/python_mysql_where.asp
    sql = "SELECT * FROM food_items WHERE dish_name = %s"
    dish = (selected_dish,)

    # Execute SQL query safely to prevent SQL Injection
    cursor.execute(sql, dish)

    # Get matching food rows from database
    foods = cursor.fetchall()

    print(foods)

    # Close cursor
    cursor.close()

    # Close database connection
    con.close()

    return jsonify({
    # Original data sent from frontend
    "received_data": data,

    # Food rows returned from database
    "foods": foods
    }), 200 
