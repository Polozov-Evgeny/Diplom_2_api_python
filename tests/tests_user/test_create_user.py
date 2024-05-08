import pytest
import requests
import allure
from test_data import user_helpers
from test_data.messages import MessagesData
from config.urls import Urls
from config.endpoints import Endpoints


class TestCreateUser:

    url = f'{Urls.BASE_URL}{Endpoints.CREATE_USER_ACCOUNT}'

    @allure.title('Успешное создание учетной записи пользователя')
    def test_create_user_account_success(self, new_user_and_registration_data):
        payload = new_user_and_registration_data
        with allure.step('Отправка запроса на регистрацию пользователя'):
            response = requests.post(self.url, data=payload)

        assert (response.status_code == 200 and response.json()['success'] == True)


    @allure.title('Невозможность зарегестрировать пользователя с уже используемым логином')
    def test_create_user_with_exist_login_failure(self, new_user_and_authorization_data):
        payload = user_helpers.generate_user_registration_data_with_exist_login(new_user_and_authorization_data[0])
        with allure.step('Отправка запроса на регистрацию пользователя с уже используемым логином'):
            response = requests.post(self.url, data=payload)

        assert (response.status_code == 403
                and response.json()['message'] == MessagesData.MESSAGE_CREATE_USER_WITH_EXIST_LOGIN)


    @allure.title('Невозможность зарегестрировать пользователя без обязательного поля')
    @pytest.mark.parametrize('incorrect_registration_data',
                             [
                                 user_helpers.generate_user_registration_data_without_required_field('email_null'),
                                 user_helpers.generate_user_registration_data_without_required_field('password_null'),
                                 user_helpers.generate_user_registration_data_without_required_field('name_null'),
                                 user_helpers.generate_user_registration_data_without_required_field('all_fields_null')
                             ],
                             ids=['without_email', 'without_password', 'without_name', 'without_all_fields'])
    def test_create_user_without_required_field_failure(self, incorrect_registration_data):
        payload = incorrect_registration_data
        with allure.step('Отправка запроса на регистрацию пользователя без обязательного поля'):
            response = requests.post(self.url, data=payload)

        assert (response.status_code == 403
                and response.json()['message'] == MessagesData.MESSAGE_CREATE_USER_WITHOUT_REQUIRED_FIELDS)
