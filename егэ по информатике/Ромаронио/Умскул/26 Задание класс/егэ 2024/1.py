f = open('task1.txt')
s = f.readline()
print(s)
mas = [16546 for i in range(10000)]
for s in f:
    read, mesto = map(int, s.split())



