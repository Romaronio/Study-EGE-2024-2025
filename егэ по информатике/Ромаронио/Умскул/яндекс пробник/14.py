# s = 625 ** 90 + 125 ** 120 - 5 * 25
#
#
# def convert_to(number,base,upper=False):
#   digits = '0123456789abcdefghijklmnopqrstuvwxyz'
#   if base > len(digits): return None
#   result = ''
#   while number > 0:
#     result = digits[number % base] + result
#     number //= base
#   return result.upper() if upper else result
# print(convert_to(s, 25).count('o'))


s = 3 * 3125**8 + 2 * 625**7 - 4 * 625**6 + 3 * 125**5 - 2 * 25**4 - 2024

res = ''
alfavit = '1234567890ABCDEFGHIJKLMNO'
while s > 0:
  res = alfavit[s % 25] + res
  s //= 25
print(res)



