class Urls:
    BASE_URL = "https://qa-scooter.praktikum-services.ru"
    COURIER_ENDPOINT = f"{BASE_URL}/api/v1/courier"
    COURIER_LOGIN_ENDPOINT = f"{BASE_URL}/api/v1/courier/login"
    ORDERS_ENDPOINT = f"{BASE_URL}/api/v1/orders"
    ORDERS_CANCEL_ENDPOINT = f"{BASE_URL}/api/v1/orders/cancel"


class ResponseMessages:
    COURIER_CREATE_INSUFFICIENT_DATA = "Недостаточно данных для создания учетной записи"

    COURIER_LOGIN_ALREADY_USED = "Этот логин уже используется"

    COURIER_LOGIN_INSUFFICIENT_DATA = "Недостаточно данных для входа"
    COURIER_ACCOUNT_NOT_FOUND = "Учетная запись не найдена"
