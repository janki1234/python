"""Accept input and show status according to condition.
@janki jodhani 26-05-2020
"""

number=input("Enter a number:")
number=int(number)
if number<0:
	print(f"{number} is negative")
elif number>0:
	print(f"{number} is positive")
