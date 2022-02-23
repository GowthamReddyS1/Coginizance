def triangle (number):
	a = number - 1
	for i in range(0, number):
		for j in range(0, a):
			print(end=" ")
		a =a - 1
		for j in range(0, i+1):
			print("* ", end="")
		print("\r")
number = 5
triangle(number)