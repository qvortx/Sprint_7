import random
import string
import requests
import allure
from faker import Faker
from data import Urls

fake = Faker(locale="ru_RU")


def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


@allure.step("Зарегистрировать нового курьера и вернуть список [login, password, firstName]")
def register_new_courier_and_return_login_password():
    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(Urls.COURIER_ENDPOINT, data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass


@allure.step("Сгенерировать словарь с данными нового курьера")
def generate_courier_payload():
    return {
        "login": f"{fake.user_name()}_{generate_random_string(5)}",
        "password": fake.password(length=10, special_chars=False),
        "firstName": fake.first_name()
    }


@allure.step("Сгенерировать данные для создания заказа")
def generate_order_payload(color=None):
    payload = {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": f"г. Москва, {fake.street_name()}, д. {fake.building_number()}",
        "metroStation": random.randint(1, 15),
        "phone": fake.phone_number(),
        "rentTime": random.randint(1, 7),
        "deliveryDate": fake.future_date(end_date="+10d").strftime("%Y-%m-%d"),
        "comment": fake.sentence(nb_words=5)
    }
    if color is not None:
        payload["color"] = color
    return payload
