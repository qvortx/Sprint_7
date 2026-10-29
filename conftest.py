import pytest
import allure
from helpers import generate_courier_payload
from courier_methods import CourierMethods
from order_methods import OrderMethods


@pytest.fixture
def registered_courier():
    """
    Создаёт курьера перед тестом, возвращает его данные
    и удаляет курьера после завершения теста.
    """
    courier_data = generate_courier_payload()
    CourierMethods.create_courier(courier_data)

    yield courier_data

    with allure.step("Пост-условие (Teardown): авторизоваться и удалить тестового курьера"):
        login_response = CourierMethods.login_courier({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })
        courier_id = login_response.json().get("id")
        CourierMethods.delete_courier(courier_id)


@pytest.fixture
def new_courier_payload():
    """
    Генерирует словарь данных для регистрации нового курьера,
    а после выполнения теста удаляет созданного курьера.
    """
    payload = generate_courier_payload()

    yield payload

    with allure.step("Пост-условие (Teardown): удалить созданного в тесте курьера"):
        login_response = CourierMethods.login_courier({
            "login": payload["login"],
            "password": payload["password"]
        })
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
            OrderMethods.cancel_order(track)
