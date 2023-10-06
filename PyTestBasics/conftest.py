import pytest


@pytest.fixture(scope="class")
def setup():
    print("I'll run first")
    yield  # Similar to tearDown
    print("This will be run after the test execution completion")


@pytest.fixture()
def dataLoad():
    print("This is for data loading fixture implementation")
    return ["Kamesh","Shanmukh","Raghu"]

@pytest.fixture(params=["Chrome","Firefox","IE"])
def crossBrowser(request):
    return request.param


@pytest.fixture(params=[("Chrome","Firefox","IE"),("Notepad","ThinkPad","Touchpage"),("Keyboard","Mouse","Screen")])
def crossBrowserMulti(request):
    return request.param