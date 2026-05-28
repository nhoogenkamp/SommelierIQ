def validate_wine(data)
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

    

    return errors
