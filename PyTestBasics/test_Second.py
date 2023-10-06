import pytest


def test_newTest():
    print("Second class test")


@pytest.mark.Smoke
def test_Assetion():
    msg = "Hello"
    assert msg == "Hi! This test failed as Strings do not match"
