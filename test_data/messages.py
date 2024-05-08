class MessagesData:

    MESSAGE_CREATE_USER_WITH_EXIST_LOGIN = 'User already exists'
    MESSAGE_CREATE_USER_WITHOUT_REQUIRED_FIELDS = 'Email, password and name are required fields'
    MESSAGE_CREATE_USER_WITH_WRONG_FIELDS = 'email or password are incorrect'
    MESSAGE_EDIT_USER_DATA_WITHOUT_AUTHORIZATION = 'You should be authorised'

    MESSAGE_CREATED_ORDER_WITHOUT_INGREDIENTS = 'Ingredient ids must be provided'
    MESSAGE_CREATED_ORDER_WITH_WRONG_INGREDIENT_HASH = 'One or more ids provided are incorrect'
    MESSAGE_GET_USER_ORDER_WITHOUT_AUTHORIZATION = 'You should be authorised'
