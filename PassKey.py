import string
import random

def gen_pass(min_len, num = True, special_char = True):
    a1 = string.ascii_letters
    a2 = string.digits
    a3 = string.punctuation

    chars = a1
    if num:
        chars += a2

    if special_char:
        chars += a3

    pwd = ""
    criteria_met = False
    contains_number = False
    contains_special = False

    while not criteria_met or len(pwd) < min_len:
        new_character = random.choice(chars)
        pwd += new_character

        if new_character in a2:
            contains_number = True
        elif new_character in a3:
            contains_special = True


        criteria_met = True
        if num:
            criteria_met = contains_number
        if special_char:
            criteria_met = criteria_met and contains_special

    return pwd

min_len = int(input ("Please enter the password length :  "))
contains_number = input("Do you want to add numbers in your password (y/n)? ").lower() == "y"
contains_special = input("Do you want to add a special character in your password (y/n)? ").lower() == "y"
pwd = gen_pass(min_len, contains_number,contains_special)
print("Here's your password : ",pwd)