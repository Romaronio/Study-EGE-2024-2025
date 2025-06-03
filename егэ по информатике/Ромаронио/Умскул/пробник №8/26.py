f = open('26.txt')
m = f.readline()
s = [int(i) for i in f]
s.sort(reverse=True)
print(s)
max_bush = []
max_bush.append(s[0])
s.remove(s[0])
for i in s[:]:
    if min(max_bush) - i >= 15:
        max_bush.append(i)
        s.remove(i)

print(len(max_bush), min(max_bush))
