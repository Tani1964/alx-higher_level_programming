#!usr/bin/python3
import random
number = random.randint(-10000, 10000)

#Get the last digit
last = int(int(repr(number)[-1]))

#change last to -ve if number is -ve
if number < 0:
	last = -abs(last)
print("Last digit of", number, "is", last, end=" ")
if last > 5:
	print("and is greater than 5")
elif last == 0:
	print("and is 0")
else:
	print("and is less than 6 and not 0")