import requests

from a09.mock.dice import roll_dice


def guess_number(num):
    result = roll_dice()
    print(result)
    print(type(result))
    if result == num:
        print("You won!")
    else:
        print("You lost!")


if __name__ == '__main__':
    # guess_number(4)
    print(type(guess_number(4)))




