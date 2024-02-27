import requests
import allure
from generate_data import *
from data import *


class TestOrderForUser:
    
    @allure.title('Получение списка заказов зарегистрированного пользователя')
    def test_get_orders_for_registry_user(self, login_user):
        get_ingredients = requests.get((Url.site + Api.ingredients ))
        ingredient_1 = get_ingredients.json()["data"][0]["_id"]
        ingredient_2 = get_ingredients.json()["data"][1]["_id"]
        ingredient_3 = get_ingredients.json()["data"][2]["_id"]
        ingredients_list = {
            "ingredients": [ingredient_1, ingredient_2, ingredient_3]
        }
        response = requests.get((Url.site + Api.orders), headers={'Autorisation': login_user.json()["accessToken"]})
        assert 200 == response.status_code and response.json()['success'] == True
        
        
    @allure.title('Получение списка заказов у незарегистрированного пользователя')   
    def test_get_order_for_noregistry_user(self,):
        response = requests.get((Url.site + Api.orders))
        assert 401 == response.status_code and response.json()["success"] == False
        
        