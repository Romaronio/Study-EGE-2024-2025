def trinity(n):
    res = []
    while n > 0:
        res = [n % 3] + res
        n = n // 3
    x = ''.join([str(x) for x in res])
    return x

res_mas = []
for n in range(1, 10000):
    n3 = trinity(n)
    n_count2 = n3.count('2')
    n3 = n3 + trinity(n_count2)
    #-------
    n_count1 = n3.count('1')
    n3 = n3 + trinity(n_count1)
    #-------
    n_count0 = n3.count('0')
    if n3.count('0') == 0:
      n3 = n3 + str('0')
    else:
      n3 = n3 + trinity(n_count0)

    res = int(n3, 3)
    if res < 1000:
      res_mas.append(res)
      res_mas.sort()
      print(max(res_mas), n)
    
