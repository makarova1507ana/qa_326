import pytest
@pytest.fixture(scope="session")
def example():
    print("\nSetup for session")
    yield
    print("\nTeardown for session")

@pytest.fixture(scope="module")
def setup():
    print("\nSetup for function")
    yield
    print("\nTeardown for function")

def test_function_1(setup):
    print("Test 1")

def test_function_2(setup):
    print("Test 2")

def test_function_3(example):
    print("Test 3")

@pytest.fixture(scope="class")
def setup2():
    print("\nSetup for class")
    yield
    print("\nTeardown for class")

class TestClass:
    def test_class_1(self, setup2):
        print("Test 1")

    def test_class_2(self, setup2):
        print("Test 2")