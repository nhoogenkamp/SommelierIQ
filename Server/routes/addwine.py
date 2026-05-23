from flask import request, jsonify
from db import get_db_connection

def add_wine():
    data = request.get_json()
    print(data)

    restaurant_id = data["restaurant_id"]
    name = data["name"]
    wine_type = data["wine_type"]
    grape = data["grape"]
    country = data["country"]
    region = data["region"]
    year = data["year"]
    bottle_type = data["bottle_type"]
    price = data["price"]
    available = data["available"]
    description = data["description"]
    #colour is always 20
    colour_score = 20
    body_score = data["body_score"]
    tannin_score = data["tannin_score"]
    acidity_score = data["acidity_score"]
    sweetness_score = data["sweetness_score"]

    con = get_db_connection()
    cursor = con.cursor(dictionary=True)
   
    # insert admin into admins table
    sql = "INSERT INTO wines (restaurant_id, name, wine_type, grape,country,region,year,bottle_type,price,available,description,colour_score,body_score,tannin_score,acidity_score,sweetness_score) " \
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (restaurant_id, name, wine_type, grape,country,region,year,bottle_type,price,available,description,colour_score,body_score,tannin_score,acidity_score,sweetness_score)

    cursor.execute(sql, values)

    con.commit()

    cursor.close()
    con.close()

    return jsonify({
        "message": "New wines added"
    }), 200    