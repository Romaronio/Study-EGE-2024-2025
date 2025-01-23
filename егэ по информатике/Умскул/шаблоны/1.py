def three(a, n):
	return(sum(a[::-1][i] * n ** i for i in range(len(a))))
