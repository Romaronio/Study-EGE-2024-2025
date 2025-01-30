n = 16
k = 0
for i1 in range(n):
	for i2 in range(i1+1, n, 2):
		for i3 in range(i2+1, n, 2):
			for i4 in range(i3+1, n, 2):
				for i5 in range(i4+1, n, 2):
					for i6 in range(i5+1, n, 2):
						for i7 in range(i6+1, n, 2):
							for i8 in range(i7+1, n, 2):
								for i9 in range(i8+1, n, 2):
									for i10 in range(i9+1, n, 2):
										for i11 in range(i10+1, n, 2):
											for i12 in range(i11+1, n, 2):
												k += 1
print(k)

