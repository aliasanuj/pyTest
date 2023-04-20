



def validate_age(age):
    if age < 0:
        raise ValueError("age cannot less than zero")
    elif age < 18:
        print("ags is less than 18")

