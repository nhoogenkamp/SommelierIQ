from flask import request, jsonify
from db import get_db_connection

def add_wine():
    data = request.get_json()

    #validations: https://www.w3schools.com/Python/trypython.asp?filename=demo_for_break
    #https://ashishsah1111.medium.com/input-validation-and-error-handling-in-flask-apis-332f4e9bc05d
    # append https://www.w3schools.com/Python/trypython.asp?filename=demo_ref_list_append2
    # f string https://www.geeksforgeeks.org/python/formatted-string-literals-f-strings-python/
    # https://www.w3schools.com/Python/trypython.asp?filename=demo_for_break

    # Validations
    fields = ["restaurant_id", "name", "wine_type", "grape", "country", "region", "year", "bottle_type", "price", "available", "description"
              , "body_score", "tannin_score", "acidity_score", "sweetness_score"]

    errors = []

    # checking if fields are not missing
    for f in fields:
        if f not in data:
            errors.append(f"{f} is required")

    # checking if restaurant_id is an int
    if not isinstance(data.get("restaurant_id"), int):
        errors.append("Restaurant_id must be a whole number")

    if errors:
        return jsonify({
            "errors": errors
        }), 400

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