#  When we create an file to use PyTest, file name either starts with test_ or ends with _test
# Python method name should starts with test
# Any test should be wrapped in method only
# Make sure we are not using same method name for multiple tests as it doesn't throw error and simply overrides the previous one with latest
import pytest


def test_firstProgramm():
    print("Hello")


# def test_firstProgramm():
#     print("Good Morning")

@pytest.mark.Smoke
def test_SecondTest():
    print("Good Morning")


@pytest.mark.skip
def test_Assetion():
    n = 4
    assert n + 2 == 6, "This is for passing assertion"


@pytest.fixture()
def setup():
    print("I'm the first test")
