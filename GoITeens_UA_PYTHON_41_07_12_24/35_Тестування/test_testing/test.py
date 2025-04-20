from main import add, minus, sign_in, add_product


def test_add():
    assert add(1, 1) == 2, "Сума повинна дорівнювати 2"
    assert add(0, 0) == 0
    assert add(2, -2) == 0
    assert add(-4, -1) == -5
    print("test_add - OK")


def test_minus():
    assert minus(5, 3) == 2
    assert minus(5.5, 3.2) == 2.3
    assert minus(5, 0) == 5
    assert minus(0, 0) == 0
    print("test_minus - OK")


def test_sign_in():
    assert sign_in("login", "password") == True, "Повинно бути True"
    assert sign_in("wrong_login", "wrong_password") == False, "Повинно бути False"
    print("test_sign_in - OK")


def test_add_product():
    assert add_product("login", "password", "name1") == "name1"
    assert add_product("login", "password", "Two word") == "Two word"
    assert add_product("login", "password", "1234") == "1234"
    assert add_product("wrong_login", "password", "product") == None
    assert add_product("login", "wrong_password", "product") == None
    assert add_product("wrong_login", "wrong_password", "product") == None
    print("test_add_product - OK")


test_add()
test_minus()
test_sign_in()
test_add_product()
print("Всі тести пройдено успішно!")
