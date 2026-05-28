from datetime import datetime

def validate_wine(data)
    #validations: https://www.w3schools.com/Python/trypython.asp?filename=demo_for_break
    #https://ashishsah1111.medium.com/input-validation-and-error-handling-in-flask-apis-332f4e9bc05d
    # append https://www.w3schools.com/Python/trypython.asp?filename=demo_ref_list_append2
    # f string https://www.geeksforgeeks.org/python/formatted-string-literals-f-strings-python/
    # https://www.w3schools.com/Python/trypython.asp?filename=demo_for_break

    # Validations for add wine
    fields = ["restaurant_id", "name", "wine_type", "grape", "country", "region", "year", "bottle_type", "price", "available", "description"
              , "body_score", "tannin_score", "acidity_score", "sweetness_score"]

    errors = []

    # checking if fields are not missing
    for f in fields:
        if f not in data:
            errors.append(f"{f} is required")

    if "restaurant_id" in data: 

        # checking if restaurant_id is an int and greater than 0
        if not isinstance(data.get("restaurant_id"), int):
            errors.append("Restaurant_id must be a whole number")
        else:    
            if data["restaurant_id"] < 1:
                errors.append("Restaurant_id must greater than 1")

    # checking if is string        
    inputstring = ["wine_type", "grape", "country", "bottle_type", "description"]
    for s in inputstring:
        if not isinstance(data.get(s), str):
            errors.append(f"{f} must be text")

    # checking if its int
    inputint = ["year", "available", "body_score", "tannin_score", "acidity_score", "sweetness_score"]
    for i in inputint:
        if not isinstance(data.get(i), int):
            errors.append(f"{f} must be a whole number")

    if "year" in data: 
       if data["year"] < 1900 or data["year"]> datetime.now().year:
                errors.append("Year is incorrect")

    if "bottle_type" in data: 
        Bottletypes = ["Glass", "Half Bottle", "Bottle", "Magnum", "Jeroboam","Melchior", "Salmanazar", "Double Magnum", "Imperial"]
        if data["bottle_type"] not in Bottletypes:
            errors.append("Incorrect bottletype")

    if "price" in data: 
        if not isinstance(data.get("price"),(int, float)):
            errors.append("Price must be a number")
        else:    
            if data["price"] < 1:
                errors.append("Price must be at least 1")

    if "available" in data: 
        availablenum = [1 , 0]
        if data["available"] not in availablenum:
            errors.append("Available is only 0 or 1")

    inputscore = ["body_score", "tannin_score", "acidity_score", "sweetness_score"]
    for i in inputscore:
        if data[i] < 0 or data[i] >20:
            errors.append(f"{i} must be between 0 and 20")    

    return errors
