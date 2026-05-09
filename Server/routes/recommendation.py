#function to calculate food and wine match 
def calculate_match(food, wine, sauce):
    total_score = 0

    # as sauces were repeatedly adding and substracting in the loop
    # creating food score variables so sauce variables don't keep adding on top of it
    # https://stackoverflow.com/questions/2465921/how-to-copy-a-dictionary-and-only-edit-the-copy

    food_body_score=food["body_score"]
    food_tannin_score=food["tannin_score"]
    food_acidity_score=food["acidity_score"]
    food_sweetness_score=food["sweetness_score"]

    if wine["wine_type"] == food["colour_wine"]:
        total_score += wine["colour_score"]

    if sauce :
         # Add sauce modifiers onto food scores
        food_body_score += sauce["body_modifier"]
        food_tannin_score += sauce["tannin_modifier"]
        food_acidity_score += sauce["acidity_modifier"]
        food_sweetness_score += sauce["sweetness_modifier"]

    # calculating body score, tanning score, acidity and sweetness difference
    # to ensure no negative numbers using abs() https://www.w3schools.com/python/ref_func_abs.asp
    body_difference = abs(food_body_score-wine["body_score"])
    total_score += 20 - body_difference

    tanin_difference = abs(food_tannin_score-wine["tannin_score"])
    total_score += 20 - tanin_difference

    acidity_difference = abs(food_acidity_score-wine["acidity_score"])
    total_score += 20 - acidity_difference

    sweetness_difference = abs(food_sweetness_score-wine["sweetness_score"])
    total_score += 20 - sweetness_difference

    return total_score    
