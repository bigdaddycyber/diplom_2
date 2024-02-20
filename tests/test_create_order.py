import requests
import allure
from generate_data import *
from data import *


class TestCreateOrder:
    
    @allure.title('Создание заказа для авторизованного пользователя с ингредиентами')
    def test_create_order_with_authorization_and_ingredients(self):
        ingredients_id = get_ingredients_id()
        token, email, user, password = create_new_user()
        ingredients = get_2_ingredients(ingredients_id)
        
        payload = {
            "ingredients": ingredients
        }
        response = requests.post((Url.site + Api.orders), headers={'Autorisation': token}, data=payload)
        assert 200 == response.status_code and response.json()['success'] == True
        generate_data_new_user.delete_user(token)
    
    @allure.title('Создание заказа для неавторизованого пользователя с игредиентами')    
    def test_create_order_without_authorization(self):
        ingredients_id = get_ingredients_id()
        ingredients = get_2_ingredients(ingredients_id)
        payload = {
            "ingredients": ingredients
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
    def test_create_order_with_incorrect_ihgredients_id(self):
        ingredient_id = get_ingredients_id()
        ingredients = get_incorrect_ingredients_id(ingredient_id)
        payload = {
            "ingredients": ingredients
        }
        responce = requests.post('https://stellarburgers.nomoreparties.site/api/orders', data=payload)
        assert responce.status_code == 500
        

        