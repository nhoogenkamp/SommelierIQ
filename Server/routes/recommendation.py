#function to calculate food and wine match 
def calculate_match(food, wine):
    total_score = 0
    if wine["wine_type"] == food["colour_wine"]:
        total_score += wine["colour_score"]

    return total_score    
