#function to calculate food and wine match 
def calculate_match(food, wine):
    total_score = 0
    if wine["wine_type"] == food["colour_wine"]:
        total_score += wine["colour_score"]

    # calculating body score difference
    # to ensure no negative numbers using abs() https://www.w3schools.com/python/ref_func_abs.asp
    body_difference = abs(food["body_score"]-wine["body_score"])
    total_score += 20 - body_difference


    return total_score    
