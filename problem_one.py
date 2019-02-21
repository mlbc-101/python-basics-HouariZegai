"""
Write a program which will find and display all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
"""

counter = 2000
while counter <= 3200:
	if counter % 7 == 0 and counter % 5 != 0:
		print(counter)
	counter+=1