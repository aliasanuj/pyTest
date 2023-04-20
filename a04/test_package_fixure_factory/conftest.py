from datetime import datetime
from a04.custom_fixture_factory_package_name.sample import Student
import pytest

@pytest.fixture
def dummy_student():
    return Student("anuj",datetime(2000,1,1),"abc", 20)

@pytest.fixture
def make_dummy_student():
    def _make_dummy_student(name, credits):
        return Student(name, datetime(2000, 1,1,) , "coe", credits)
    return _make_dummy_student
