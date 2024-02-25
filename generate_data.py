import requests
import random
import string


def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    
def generate_email():
    email = generate_random_string
    return email   


def generate_data_new_user():
    email = generate_email()
    password = generate_random_string(10)
    user = generate_random_string(10)
    return email, password, user

def create_new_user():
    email, user, password = generate_data_new_user()
    payload = {
        "email": email,
        "password": password,
        "name": user
    }
    response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data=payload )
    token = response.json()["accessToken"]
    return token, email, password, user


def get_ingredients_id():
    responce = requests.get('https://stellarburgers.nomoreparties.site/api/ingredients')
    id_ingredients = []
    ingredients_data = responce.json()["data"]
    for ingredient in ingredients_data:
        ingredients_data.append(ingredients_data["_id"])
    return id_ingredients    
    
def get_2_ingredients(ingredients_data):
    ingredients = []
    for i in range[2]:
        while True:
            n = generate_random_string(0, len(ingredients_data), -1)
            if ingredients[n] not in ingredients:
                ingredients.append(id_ingredients[n])
                break
    return ingredients        

def get_incorrect_ingredients_id(id_ingredients):
    ingredients = []
    m = generate_random_string(0, len(id_ingredients), -1)
    ingredients.append(id_ingredients[m] + 'mmm')
    return ingredients

def create_order_for_authorisation_user(token):
    id_ingredients = get_ingredients_id()
    ingredients = get_2_ingredients(id_ingredients)
    payload = {
        "ingredients": ingredients
    }
    responce = requests.post('https://stellarburgers.nomoreparties.site/api/orders', headers={'Autorisation': token}, data=payload)
    return responce.json()['order']['number']

def create_two_orders(token):
    order = [create_order_for_authorisation_user(token), create_order_for_authorisation_user(token)]
    return order

def delete_user(token):
    requests.delete('https://stellarburgers.nomoreparties.site/api/auth/user', headers={"Authorization": token})