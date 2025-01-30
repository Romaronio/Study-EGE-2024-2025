# def F(n):
# 	if n == 1:
# 		return 2
# 	if n > 1:
# 		return F(n -1) + 3
# print(F(3))

# def G(n):
# 	if n == 1:
# 		return 1
# 	if n > 1:
# 		return G(n - 1) * 2
# print(G(4))

def H(n):
	if n == 0:
		return 5
	if n > 0:
		return H(n - 1) + 2
print(H(2))