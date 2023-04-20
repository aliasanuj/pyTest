import sys

import pytest

from a06.markers_package_name.sample import adding

@pytest.mark.skip(reason="just wanna skip")
def test_add():
    assert adding(1,2) == 3

@pytest.mark.skipif(sys.version_info > (3, 7), reason = "python is greater than 3.7 version")
def test_add01():
    assert adding("1","2") == "12"

@pytest.mark.xfail
def test_xchvbhcbhx():
    assert adding([1],[2]) == [1,2]
    raise Exception()

@pytest.mark.xfail(sys.platform == "linux", reason = "dont run on liux") #try win32 instead of linux
def test_xchvbhcbhx():
    assert adding([1],[2]) == [1,2]
    raise Exception()

def test_xchvbhcbhx():
    assert adding(1,2) == 3

print(sys.platform)
