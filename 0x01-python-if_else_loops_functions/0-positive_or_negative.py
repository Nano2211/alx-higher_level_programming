#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
if number > 0:
	print("is positive")
elif number == 0:
	print("is zero")
	break
else print("is negative")
