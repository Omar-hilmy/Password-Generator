import random
import string

def make_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = "".join(random.choice(chars) for _ in range(length))
    return password

length = int(input("How many characters? (example: 12): "))
print("Your password is:", make_password(length))
