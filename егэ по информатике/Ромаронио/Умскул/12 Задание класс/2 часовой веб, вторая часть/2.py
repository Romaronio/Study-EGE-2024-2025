for n in range(91, 1000):
	s = "3" * n
	while "333" in s:
		s = s.replace("333", "1", 1)
		s = s.replace("111", "3", 1)
	if s == "133":
		print(n)
		break