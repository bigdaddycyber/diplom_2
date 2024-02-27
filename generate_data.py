import requests
import random
import string


def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    
def get_2_ingredients(ingredients_data):
    ingredients = []
    for i in range[2]:
        while True:
            n = generate_random_string(0, len(ingredients_data), -1)
            if ingredients[n] not in ingredients:
                ingredients.append(ingredients[n])
                break
    return ingredients        

def get_incorrect_ingredients_id(id_ingredients):
    ingredients = []
    m = generate_random_string(0, len(id_ingredients), -1)
    ingredients.append(id_ingredients[m] + 'mmm')
    return ingredients

