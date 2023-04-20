from datetime import datetime
import pytest
from a08.parametrizing_fixtures_packageName.sample import is_eligible_for_degree

def test_student_get_age(dummy_student):
    dummy_student_age = (datetime.now() - dummy_student.dob).days // 365
    assert dummy_student.get_age() == dummy_student_age

def test_student_get_credits(dummy_student):
    assert dummy_student.get_credits() == 21 # put 23 and check

def test_student_is_elligible_true(make_dummy_student):
    assert is_eligible_for_degree(make_dummy_student("sam",19)) is False

def test_student_is_elligible_false(make_dummy_student):
    assert is_eligible_for_degree(make_dummy_student("sam",21)) is True

@pytest.mark.parametrize("credits,expected", [(19, False), (21, True)])
def test_student_is_elligible_anyname(make_dummy_student, credits, expected):
    assert is_eligible_for_degree(make_dummy_student("sam",credits)) is expected

@pytest.mark.parametrize("dummy_student,expected",
                         [(19, False), (21, True)],
                         indirect=["dummy_student"],
                         ids=["inelgible","iligible"])
def test_student_is_elligible_anyname(dummy_student,expected):
    assert is_eligible_for_degree(dummy_student) is expected
