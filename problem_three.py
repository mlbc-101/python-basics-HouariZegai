"""Write a program that solves second degree equation of the form ax^2 +bx + c = 0."""

a = int(input('Type a: '))
b = int(input('Type b: '))
c = int(input('Type c: '))

delta = b ** 2 - 4 * a * c

if delta < 0:
	print("The is no solution because delta < 0 !")
elif delta == 0:
	print('solution is : ', -b / 2*a)
else:
	print('solution 1 is: ', (-b - delta ** (1.0 / 2)) / 2 * a)
	print('solution 2 is: ', (-b + delta ** (1.0 / 2)) / 2 * a)