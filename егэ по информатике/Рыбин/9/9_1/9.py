f = open('09.txt')  # КЕГЭ №7335
k = 0
for s in f:
    n = [int(x) for x in s.split()]
    a = (len(set(n)) == len(n)) and n.count(int((max(n)+min(n))/2)) >= 1
    pt = [x for x in n if n.count(x) >= 2]
    b = (len(set(n)) != len(n)) and (sum([x**2 for x in pt if len(pt) != 0]) < sum([x**2 for x in (set(n) - set(pt))]))
    if (a == 1 and b == 0) or (a == 0 and b == 1):
        k += 1
print(k)

# P.S ChatGPT - пидорас
                                     
        
