import pytest
import requests
from faker import Faker
from generate_data import generate_random_string
from data import Url, Api

fake = Faker()

@pytest.fixture()
def login_user():

    email = 'testtestcucaracha@gmail.com'
    password = 'testest123'
    payload = {
        "email": email,
        "password": password,
        }
    response = requests.post(Url.site + Api.login, data=payload)
    return response


@pytest.fixture()
def create_new_user():
    email = fake.email()
    password = fake.password()
    name = fake.first_name()
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    response = requests.post(Url.site + Api.register, data=payload)
    token = response.json()["accessToken"]
    yield response
    requests.delete(Url.site + Api.user, headers={'Autorisation': token}, data=payload)


