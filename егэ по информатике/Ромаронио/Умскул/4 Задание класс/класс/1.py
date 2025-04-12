from itertools import *
def is_fano(code_in_list, code):
    for code_list in code_in_list:
      if code_list.startswith(code) or code.startswith(code_list):
        return False
    return True


code_in_list = ['1', '010', '00']
possible = []
for i in range(1, 6):
  for bits in product('01', repeat=i):
    possible.append(''.join(bits))
print(possible)


for psd_code in possible:
  if is_fano(code_in_list, psd_code):
    print(psd_code)



