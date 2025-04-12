

alfa = '0123456789abcdefghi'
for x in alfa:
  if (int(f'98897{x}21', 19) + int(f'2{x}923', 19)) % 18 == 0:
    print(x)




print((int('98897621', 19) + int('26923', 19)) / 18)