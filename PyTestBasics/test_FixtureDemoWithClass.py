import pytest

#from PyTestBasics.conftest import setup


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_firstTest(self):
        print("Actual Test")

    def test_firstTest1(self):
        print("Actual Test1")

    def test_firstTest2(self):
        print("Actual Test2")

    def test_firstTest3(self):
        print("Actual Test3")

    def test_firstTest4(self):
        print("Actual Test4")
