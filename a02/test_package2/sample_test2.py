import pytest

from a02.packageName2.sample2 import validate_age

def test_dcbdhcvvalidate_age():
    validate_age(-10)

def test_diurfy_age():
    with pytest.raises(ValueError):
        validate_age(-1)

def test_hdcv9e8r7_age():
    with pytest.raises(ValueError) as exception_info:
        validate_age(-1)
    assert str(exception_info.value) == "age cannot less than zero"

def test_hdcv9_age():
    with pytest.raises(ValueError, match="age cannot less than zero"):
        validate_age(-1)


class Test_FirstCapital():
    def test_dcbdhcvvalidate_age(self):
        validate_age(10)

