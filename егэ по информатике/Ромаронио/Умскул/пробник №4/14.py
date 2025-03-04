alfa = '0123456789ABCDEF'
for x in alfa:
  if (int(f'{x}432', 16) + int(f'234{x}', 16)) % 15 == 0:
    print((int(f'{x}432', 16) + int(f'234{x}', 16)) / 15)


print(int('6432', 16))
print(int('2346', 16))

print((9030 + 25650) / 15)