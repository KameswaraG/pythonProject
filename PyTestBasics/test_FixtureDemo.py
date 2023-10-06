import pytest


# @pytest.fixture()
# def setup():
#     print("I'll run first")
#     yield  # Similar to tearDown
#     print("This will be run after the test execution completion")


def test_firstTest(setup):
    print("Actual Test")
