def add(a: float, b: float) -> int|float:
    return a + b


def minus(a: float, b: float) -> float|int:
    return a - b


def sign_in(login: str, password: str) -> bool:
    if login == "login" and password == "password":
        return True
    return False


def add_product(login: str, password: str, product: str) -> str|None:
    if sign_in(login, password):
        return product
    return
