import string
f = open('24.txt')
s = f.readline()
for i in range(len(s)):
  if s[i] in string.ascii_uppercase:
    s = s.replace(s[i], 'A')

s = s.split('A')
print(len(max(s, key=len)))


