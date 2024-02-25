import pytest
from selenium import webdriver
import requests



@pytest.fixture(scope="function")
def delete_user(token):
    requests.delete('https://stellarburgers.nomoreparties.site/api/auth/user', headers={"Authorization": token})
    return delete_user


