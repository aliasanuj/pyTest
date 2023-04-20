from datetime import datetime

print("class student")
class Student:
    print("student init constructer")
    def __init__(self,name, dob , branch, credits):
        self.name = name
        self.dob = dob
        self.branch = branch
        self.credits = credits

    def get_age(self):
        return (datetime.now() - self.dob).days // 365

    def get_credits(self):
        return self.credits

def is_eligible_for_degree(student):
    return student.get_credits() >= 20


# from datetime import  datetime
# def Student(aa,bb,cc,dd):
#     print("student function")
#     pass
