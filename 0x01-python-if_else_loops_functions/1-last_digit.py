#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
new_num = str(number)[-1]
if int(new_num) > 5:
    print(f"Last digit of {number} is {new_num} and is greater than 5")
elif int(new_num) < 6 and int(new_num) != 0:
    print(f"Last digit of {number} is {new_num} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {new_num} and is 0")
