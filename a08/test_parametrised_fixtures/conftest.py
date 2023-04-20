from datetime import datetime
from a08.parametrizing_fixtures_packageName.sample import Student
import pytest

# working in def test_student_get_credits(dummy_student): line number 9 in test_efg
# @pytest.fixture()
# def dummy_student():
#     return Student("anuj",datetime(2000,1,1),"branch",21)

# working
@pytest.fixture(params=[19, 21, 10 ], ids = ["eligible", "ineligible", "abc"])
def dummy_student(request):
    return Student("anuj",datetime(2000,1,1),"branch",request.param)

@pytest.fixture
def make_dummy_student():
    def _make_dummy_student(name, credits):
        return Student(name, datetime(2000, 1,1,) , "coe", credits)
    return _make_dummy_student
