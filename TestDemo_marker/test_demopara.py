import pytest
class Testdemo:
    @pytest.mark.parametrize("data",[5,6,7])
    def test_nogt(self,data):
        if data>5:
            assert True
        else:
            assert False