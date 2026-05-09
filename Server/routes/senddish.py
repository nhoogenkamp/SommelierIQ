from flask import request, jsonify
from db import get_db_connection
from routes.recommendation import calculate_match


# Function handles POST request from frontend
def send_dish():

    # Reading the JSON sent
    data = request.get_json()
    # Print received data in Flask terminal
    print(data)

    # Get the value stored in the key "dish" and "sauce"
    selected_dish = data["dish"]
    selected_sauce = data["sauce"]

    con = get_db_connection()
    cursor = con.cursor(dictionary=True)

    # SQL query searches for matching food item : https://www.w3schools.com/python/python_mysql_where.asp
    sql = "SELECT * FROM food_items WHERE dish_name = %s"
    dish = (selected_dish,)

    # Execute SQL query safely to prevent SQL Injection
    cursor.execute(sql, dish)

    # Get matching food rows from database
    foods = cursor.fetchone()

    print(foods)

    if selected_sauce != "":
        sauce_sql = "SELECT * FROM sauces WHERE name = %s"
        sauce = (selected_sauce,)
        cursor.execute(sauce_sql, sauce)
        sauces = cursor.fetchone()

    print(sauces)    


    #sql query to get all wines 
    wine_sql = "SELECT * FROM wines"
    cursor.execute(wine_sql)
    wines = cursor.fetchall()

    #creating an empty list to store recommendations
    recommendations = []
    
    #looping through wines and calculate each wine based on food ordered 
    for wine in wines:
        score = calculate_match(foods,wine,sauces)
        wine["match_percentage"] = score
        recommendations.append(wine)

    # change the order of recommendations based on match percentage: https://www.w3schools.com/python/trypython.asp?filename=demo_lambda_sorted
    recommendations = sorted (recommendations, key=lambda x: x["match_percentage"],reverse=True)
    print(recommendations)

    # Close cursor
    cursor.close()

    # Close database connection
    con.close()

    return jsonify({
    # Original data sent from frontend
    "received_data": data,

    # Food rows returned from database
    "foods": foods,

    # wines rows returned from database
    "wines": wines,   

    # recommendations returned from from calculations and added match percentage
    "recommendations": recommendations 
    }), 200 
