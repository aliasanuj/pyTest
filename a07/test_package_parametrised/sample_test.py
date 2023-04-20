from a07.parametrized_package_name.sample import adding
import pytest

def test_add():
    assert adding(1,2) == 3

def test_add01():
    assert adding("1","2") == "12"

def test_xchvbhcbhx():
    assert adding(1,2) == 3

def test_addinglist():
    assert adding([1,2],[3]) ==[1,2,3]

@pytest.mark.parametrize("a,b,c", [(1,2,3),("a","b","ab"), ([1,2],[3],[1,2,3])],ids=["nun","str","list"])
def test_8r7e7gfher(a,b,c):
    assert adding(a,b) == c

class Test_sample():
    def test_addsdvdf(self):
        assert adding(1, 2) == 3

    def test_add01dfvd(self):
        assert adding("1", "2") == "12"

    def test_xchvbhcbhxdfvd(self):
        assert adding(1, 2) == 3

