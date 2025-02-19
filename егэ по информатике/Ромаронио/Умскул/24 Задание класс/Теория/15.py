import re
f = open('24.15.txt')
s = f.readline()
buff = ''

# buff = s[0]
# res_mas = []
# for i in range(len(s)):
#   if s[i] < s[i - 1]:
#     buff += s[i]
#   else:
#     res_mas.append(buff)
#     buff = s[i]
# print(len(max(res_mas, key=len)))

is_ok = re.findall(r"9?8?7?6?5?4?3?2?1?0?", s)
print(max(is_ok, key=len))
