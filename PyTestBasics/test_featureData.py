import pytest


@pytest.mark.usefixtures("dataLoad")
class TestDatExample:

    def test_editProfile(self,dataLoad):
        print(dataLoad)