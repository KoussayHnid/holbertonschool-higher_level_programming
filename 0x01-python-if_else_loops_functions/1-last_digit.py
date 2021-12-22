#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
degit = abs(number)
degit = degit % 10
if number < 0:
    degit = degit * (-1)
if degit > 5:
    print("Last digit of", number, "is", degit, "and is greater than 5")
elif degit == 0:
    print("Last digit of", number, "is", degit, "and is 0")
else:
    print("Last digit of", number, "is", degit, "and is less than 6 and not 0")
