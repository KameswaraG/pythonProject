import pytest

from PyTestBasics.BaseClass import BaseClass


class TestParam(BaseClass):
    def test_crossBrowser(self,crossBrowser):
        print(crossBrowser)




    @pytest.mark.usefixtures("crossBrowserMulti")
    def test_crossMultiParam(self,crossBrowserMulti):
        log =self.getLogger()
        for item in crossBrowserMulti:
            log.info(item)
