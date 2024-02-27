import requests
import allure
from generate_data import *
from data import *


class TestCreateOrder:
    
    @allure.title('Создание заказа для авторизованного пользователя с ингредиентами')
    def test_create_order_with_authorization_and_ingredients(self, login_user):
        get_ingredients = requests.get((Url.site + Api.ingredients ))
        ingredient_1 = get_ingredients.json()["data"][0]["_id"]
        ingredient_2 = get_ingredients.json()["data"][1]["_id"]
        ingredient_3 = get_ingredients.json()["data"][2]["_id"]
        payload = {
            "ingredients": [ingredient_1, ingredient_2, ingredient_3]
        }
        
        response = requests.post((Url.site + Api.orders), data=payload)
        assert 200 == response.status_code and response.json()['success'] == True
        
    
    @allure.title('Создание заказа для неавторизованого пользователя с игредиентами')    
    def test_create_order_without_authorization(self):
        get_ingredients = requests.get((Url.site + Api.ingredients ))
        ingredient_1 = get_ingredients.json()["data"][0]["_id"]
        ingredient_2 = get_ingredients.json()["data"][1]["_id"]
        payload = {
            "ingredients": [ingredient_1, ingredient_2]
        }
        response = requests.post((Url.site + Api.orders), data=payload)
        assert 200 == response.status_code and response.json()['success'] == True
        
        
    @allure.title('Создание заказа без игредиентов')    
    def test_create_order_without_igredients(self):
        payload = {
            "ingredients": []
        }
        response = requests.post((Url.site + Api.orders), data=payload)
        assert 400 == response.status_code and response.json() == {
                                                                   "success": False,
                                                                   "message": "Ingredient ids must be provided"
                                                                   }
        
        
    @allure.title('Создание заказа с некорректными ингредиентами')
    def test_create_order_with_incorrect_ihgredients_id(self, login_user):
        payload = {
            "ingredients": ["534534243232g4234"]
        }
        responce = requests.post((Url.site + Api.orders), data=payload)
        assert 500 == responce.status_code
        

        