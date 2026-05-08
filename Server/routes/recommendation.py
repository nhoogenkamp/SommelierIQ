#function to calculate food and wine match 
def calculate_match(food, wine, sauce):
    total_score = 0
    if wine["wine_type"] == food["colour_wine"]:
        total_score += wine["colour_score"]

    if sauce :
         # Add sauce modifiers onto food scores
        food["body_score"] += sauce["body_modifier"]
        food["tannin_score"] += sauce["tannin_modifier"]
        food["acidity_score"] += sauce["acidity_modifier"]
        food["sweetness_score"] += sauce["sweetness_modifier"]

    # calculating body score, tanning score, acidity and sweetness difference
    # to ensure no negative numbers using abs() https://www.w3schools.com/python/ref_func_abs.asp
    body_difference = abs(food["body_score"]-wine["body_score"])
    total_score += 20 - body_difference

    tanin_difference = abs(food["tannin_score"]-wine["tannin_score"])
    total_score += 20 - tanin_difference

    acidity_difference = abs(food["acidity_score"]-wine["acidity_score"])
    total_score += 20 - acidity_difference

    sweetness_difference = abs(food["sweetness_score"]-wine["sweetness_score"])
    total_score += 20 - sweetness_difference

    return total_score    
