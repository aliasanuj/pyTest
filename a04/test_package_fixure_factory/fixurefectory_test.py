from datetime import datetime
from a04.custom_fixture_factory_package_name.sample import get_topper

def test_student_get_age(dummy_student):
    dummy_student_age = (datetime.now() - dummy_student.dob).days // 365
    assert dummy_student.get_age() == dummy_student_age

def test_student_get_credits(dummy_student):
    assert dummy_student.get_credits() == 20

def test_get_topper(make_dumy_student):
    students = [
        make_dumy_student("bbb", 21),
        make_dumy_student("ccc", 24),
        make_dumy_student("aaa", 27),
    ]
    topper = get_topper(students)
    assert topper == students[2]


