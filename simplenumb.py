	def simplenum(N):

		simple = set (range(1,N))
		for i in range (2, int(math.sqrt(N))):

			if i in simple:

				simple -= set(range(2*i, N, i))

		return simple

	print(simplenum(225))