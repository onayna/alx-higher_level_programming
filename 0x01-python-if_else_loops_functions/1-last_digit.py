#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Print the last digit of the number
print("Last digit of", number, "is", abs(number) % 10, end=' ')

# Check conditions for the last digit
if abs(number) % 10 > 5:
    print("and is greater than 5")
elif abs(number) % 10 == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
