"""Write a program which can compute the factorial of a given numbers."""

number = int(input("Type number: "))

if(number < 0):
	print("Invalid input (negative number!)")
else:
	result = 1
	index = 2
	while index <= number:
		result *= index
		index += 1
	
	print(number, '! = ', result)