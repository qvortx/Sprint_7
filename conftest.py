import pytest
import allure
from helpers import register_new_courier_and_return_login_password, generate_courier_payload
from courier_methods import CourierMethods
from order_methods import OrderMethods


@pytest.fixture
def registered_courier():
    """
    Создаёт курьера перед тестом с помощью метода из задания,
    возвращает его данные и удаляет курьера после завершения теста.
    """
    login_pass = register_new_courier_and_return_login_password()
    courier_data = {
        "login": login_pass[0],
        "password": login_pass[1],
        "firstName": login_pass[2]
    }

    yield courier_data

    with allure.step("Пост-условие (Teardown): авторизоваться и удалить тестового курьера"):
        login_response = CourierMethods.login_courier({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        if login_response.status_code == 200:
            courier_id = login_response.json().get("id")
            CourierMethods.delete_courier(courier_id)


@pytest.fixture
def new_courier_payload():
    """
    Генерирует словарь данных для регистрации нового курьера,
    а после выполнения теста проверяет, был ли он создан, и удаляет его.
    """
    payload = generate_courier_payload()

    yield payload

    with allure.step("Пост-условие (Teardown): удалить созданного в тесте курьера"):
        login_response = CourierMethods.login_courier({
            "login": payload["login"],
            "password": payload["password"]
        })
        if login_response.status_code == 200:
            courier_id = login_response.json().get("id")
            CourierMethods.delete_courier(courier_id)


@pytest.fixture
def order_cleanup():
    """
    Хранит трек-номер созданного в тесте заказа и отменяет его в пост-условии.
    """
    tracks = []

    yield tracks

    with allure.step("Пост-условие (Teardown): отменить созданный тестовый заказ"):
        for track in tracks:
            if track:
                OrderMethods.cancel_order(track)
