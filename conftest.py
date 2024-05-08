import pytest
from test_data import user_helpers, order_helpers


@pytest.fixture(scope='function')
def new_user_and_registration_data():
    registration_data = user_helpers.generate_user_data()
    yield registration_data
    tokens = user_helpers.login_user_and_return_tokens(registration_data)
    user_helpers.delete_user_account(tokens['accessToken'])


@pytest.fixture(scope='function')
def new_user_and_authorization_data():
    authorization_data = user_helpers.register_new_user_and_return_authorization_data()
    login_data = authorization_data[0]
    tokens = authorization_data[1]
    yield login_data, tokens
    user_helpers.delete_user_account(tokens['accessToken'])


@pytest.fixture(scope='function')
def new_user_with_orders(new_user_and_authorization_data):
    order_helpers.add_user_orders(new_user_and_authorization_data[1])
    yield new_user_and_authorization_data[1]
