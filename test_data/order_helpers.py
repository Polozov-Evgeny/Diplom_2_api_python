import random
import requests
import allure
from config.urls import Urls
from config.endpoints import Endpoints


@allure.step('Генерация списка ингридиентов для заказа')
def generate_ingredient_list():
    url = f'{Urls.BASE_URL}{Endpoints.GET_INGREDIENTS}'
    response = requests.get(url)
    ingredient_list = []
    for i in range(random.randint(1, 3)):
        ingredient = response.json()['data'][random.randint(0, len(response.json()['data'])-1)]['_id']
        ingredient_list.append(ingredient)
    return ingredient_list


@allure.title('Генерация и добавление заказазов пользователя')
def add_user_orders(tokens):
    url = f'{Urls.BASE_URL}{Endpoints.CREATE_ORDER}'
    headers = {'Authorization': tokens['accessToken']}
    payload = {'ingredients': generate_ingredient_list()}
    for i in range(random.randint(1, 2)):
        requests.post(url, headers=headers, data=payload)
