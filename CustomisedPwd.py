import random

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!£$%^&*()_-+={}[]#~:;@'<,>.?/\|`¬"

pwd_num = int(input("No. of passwords: "))
length = int(input("Password length? "))

while True:
    if length <= 6:
        print("That is a very short password! I recommend you make it longer!")
        length = int(input("What is your new password length? "))
    else:
        break

for p in range(pwd_num):
    password = " "
    for c in range(length):
        password += random.choice(chars)
    print(password)
