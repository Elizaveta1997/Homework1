
	a=int(input("Введи число a="))
	b=int(input("Введи число b="))
	Y = []

	for i in range(a,b+1):

		if i%5==0:
			Y.append(i)

	for i in Y:
		print(i)
