from flask import request, jsonify
from db import get_db_connection
from routes.recommendation import calculate_match


# Function handles POST request from frontend
def send_dish():

    # Reading the JSON sent
    data = request.get_json()
    # Print received data in Flask terminal
    print(data)

    con = get_db_connection()
    cursor = con.cursor(dictionary=True)

    # Get the value stored in the key both dishes and sauces
    selected_dishes = data["dishes"]

    individual_recommendations = []
    combined_recommendations = []

    for selected in selected_dishes:

        selected_dish = selected["dish"]
        selected_sauce = selected["sauce"]

        # SQL query searches for matching food item : https://www.w3schools.com/python/python_mysql_where.asp
        sql = "SELECT * FROM food_items WHERE dish_name = %s"
        dish = (selected_dish,)

        # Execute SQL query safely to prevent SQL Injection
        cursor.execute(sql, dish)

        # Get matching food rows from database
        foods = cursor.fetchone()

        print(foods)

        sauces = None

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
            
            # creating a copy to sent multiple back: https://www.w3schools.com/python/ref_list_copy.asp
            wine_result = wine.copy()
            wine_result["match_percentage"] = score
            recommendations.append(wine_result)

        # change the order of recommendations based on match percentage: https://www.w3schools.com/python/trypython.asp?filename=demo_lambda_sorted
        recommendations = sorted (recommendations, key=lambda x: x["match_percentage"],reverse=True)
        print(recommendations)

        individual_recommendations.append({
            "dish": selected_dish,
            "sauce": selected_sauce,
            "recommendations": recommendations 
    })
    print(individual_recommendations)

    # calculate combined recommendations if more than 1 dish selected
    if len(selected_dishes) > 1:

        # loop through wines
        for i in range(len(wines)):

            total_score = 0

            # loop through every dish recommendation group
            for group in individual_recommendations:

                total_score += group["recommendations"][i]["match_percentage"]

            # calculate average score
            average_score = total_score / len(selected_dishes)

            # create wine copy
            wine_result = wines[i].copy()

            # replace score with average
            wine_result["match_percentage"] = round(average_score)

            combined_recommendations.append(wine_result)

        # sort combined recommendations
        combined_recommendations = sorted(
            combined_recommendations,
            key=lambda x: x["match_percentage"],
            reverse=True
        )

    print(combined_recommendations)

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
    "recommendations": individual_recommendations
    }), 200 
