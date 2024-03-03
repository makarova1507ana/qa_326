import pytest
@pytest.fixture()
def message():
    print("запуск теста")

def test1(message):
    pass

def test2():
    pass