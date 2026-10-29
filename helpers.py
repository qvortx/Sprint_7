import random
import string
import allure
from faker import Faker

fake = Faker(locale="ru_RU")


def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


@allure.step("Сгенерировать словарь с данными нового курьера")
def generate_courier_payload():
    return {
        "login": f"{fake.user_name()}_{generate_random_string(5)}",
        "password": fake.password(length=10, special_chars=False),
        "firstName": fake.first_name()
    }


@allure.step("Сгенерировать данные для создания заказа")
def generate_order_payload(color):
    return {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": f"г. Москва, {fake.street_name()}, д. {fake.building_number()}",
        "metroStation": random.randint(1, 15),
        "phone": fake.phone_number(),
        "rentTime": random.randint(1, 7),
        "deliveryDate": fake.future_date(end_date="+10d").strftime("%Y-%m-%d"),
        "comment": fake.sentence(nb_words=5),
        "color": color
    }
