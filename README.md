## **Дипломный проект "Яндекс Практикум". Часть 2: API**

### Автоматизация тестирования API "Stellar Burgers"

1. Ссылка на сайт: *https://stellarburgers.nomoreparties.site/*
2. Документация API: *https://code.s3.yandex.net/qa-automation-engineer/python-full/diploma/api-documentation.pdf?etag=3403196b527ca03259bfd0cb41163a89/*
3. Основа для написания автотестов: *Pytest*, *Requests*
4. В автотестах используются: фикстуры и параметризация
5. Отчет о тестировании: *Allure*

**Установка Pytest:**
````
pip install pytest
````

**Установка Requests:**
````
pip install requests
````

**Установка Faker:**
````
pip install Faker
````

**Запуск автотестов:**
````
pytest -v
````

**Отчет о тестировании Allure:**
````
pip install allure-pytest
````
````
pytest tests --alluredir=allure_results
````
````
allure serve allure_results
````
