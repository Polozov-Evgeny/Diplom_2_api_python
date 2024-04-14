import requests
import allure
from faker import Faker
from config.urls import Urls
from config.endpoints import Endpoints


@allure.step('Генерация данных пользователя')
def generate_user_data():
    fake = Faker()
    user_data = {
        'email': fake.email(),
        'password': fake.password(),
        'name': fake.name()
    }
    return user_data


@allure.step('Регистрация нового пользователя и возвращение данных для авторизации')
def register_new_user_and_return_login_data():
    registration_data = generate_user_data()
    url = f'{Urls.BASE_URL}{Endpoints.CREATE_USER_ACCOUNT}'
    response = requests.post(url, data=registration_data)
    if response.status_code == 200 and response.json()['success'] == True:
        login_data = {
            'email': registration_data['email'],
            'password': registration_data['password']
        }
        return login_data
    else:
        print('Проблема с регистрацией пользовательского аккаунта')


@allure.step('Регистрация нового пользователя и возвращение токенов')
def register_new_user_and_return_tokens():
    registration_data = generate_user_data()
    url = f'{Urls.BASE_URL}{Endpoints.CREATE_USER_ACCOUNT}'
    response = requests.post(url, data=registration_data)
    if response.status_code == 200 and response.json()['success'] == True:
        registration_tokens = {
            'accessToken': response.json()['accessToken'],
            'refreshToken': response.json()['refreshToken']
        }
        return registration_tokens
    else:
        print('Проблема с регистрацией пользовательского аккаунта')


@allure.step('Авторизация пользователя и возвращение токенов')
def login_user_and_return_tokens(login_data):
    url = f'{Urls.BASE_URL}{Endpoints.LOGIN_USER}'
    response = requests.post(url, data=login_data)
    if response.status_code == 200 and response.json()['success'] == True:
        login_tokens = {
            'accessToken': response.json()['accessToken'],
            'refreshToken': response.json()['refreshToken']
        }
        return login_tokens
    else:
        print('Проблема с авторизацией пользователя')


@allure.step('Удаление учетной записи пользователя')
def delete_user_account(access_token):
    url = f'{Urls.BASE_URL}{Endpoints.DELETE_USER_ACCOUNT}'
    response = requests.delete(url, headers={'Authorization': access_token})
    if not (response.status_code == 202 and response.json()['success'] == True):
        print('Проблема с удалением пользовательского аккаунт')


@allure.step('Генерация данных для регистрации пользователя с уже используемым логином')
def generate_user_registration_data_with_exist_login(user_login_data):
    registration_data_with_exist_login = generate_user_data()
    registration_data_with_exist_login['email'] = user_login_data['email']
    return registration_data_with_exist_login


@allure.step('Генерация данных для регистрации пользователя без обязательного поля')
def generate_user_registration_data_without_required_field(required_field):
    incorrect_registration_data = generate_user_data()
    if required_field == 'email_null':
        incorrect_registration_data['email'] = None
    elif required_field == 'password_null':
        incorrect_registration_data['password'] = None
    elif required_field == 'name_null':
        incorrect_registration_data['name'] = None
    else:
        incorrect_registration_data = {}
    return incorrect_registration_data


@allure.step('Генерация данных для авторизации пользователя с некорректными полями')
def generate_user_login_data_with_wrong_field(wrong_field, login_data):
    fake = Faker()
    if wrong_field == 'email':
        incorrect_login_data = dict(email=fake.email(), password=login_data['password'])
    elif wrong_field == 'password':
        incorrect_login_data = dict(email=login_data['email'], password=fake.password())
    else:
        incorrect_login_data = dict(email=fake.email(), password=fake.password())
    return incorrect_login_data
