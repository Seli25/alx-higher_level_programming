#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_num = ((number * -1) % 10) * -1
if (abs(number) % 10) > 5:
    print(f"Last digit of {number:d} is {last_num:d} and is greater than 5")
elif (abs(number) % 10) == 0:
    print(f"Last digit of {number:d} is {last_num:d} and is 0")
else:
    print(f"Last digit of {number:d} is {last_num:d} and is less than 6 and not 0")
