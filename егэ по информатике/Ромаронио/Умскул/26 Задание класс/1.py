# f = open('26.1.txt')
# s = f.read().split('\n')
# Towar_so_skidkoy = []
# Towar_bez_skidki = []
# for i in range(len(s) - 1):
#   if int(s[i]) > 120:
#     Towar_so_skidkoy.append(s[i])
#   else:
#     Towar_bez_skidki.append(s[i])
#
# Sort_Towar_so_skidkoy = []
# for i in Towar_so_skidkoy:
#     Sort_Towar_so_skidkoy.append(int(i))
#     Sort_Towar_so_skidkoy = sorted(Sort_Towar_so_skidkoy)
# print(Sort_Towar_so_skidkoy)
#
#
# Towar_s_Uzhe_deistvuushei_skidkoy = []
# for i in range(len(Sort_Towar_so_skidkoy)):
#   if len(Towar_s_Uzhe_deistvuushei_skidkoy) < len(Sort_Towar_so_skidkoy) / 2:
#     Towar_s_Uzhe_deistvuushei_skidkoy.append(round(Sort_Towar_so_skidkoy[i] * 0.25))
# print(Towar_s_Uzhe_deistvuushei_skidkoy)
#
# Pochti_res_mas = Towar_bez_skidki + Towar_s_Uzhe_deistvuushei_skidkoy + Sort_Towar_so_skidkoy[:len(Towar_s_Uzhe_deistvuushei_skidkoy)]
#
# res_mas = []
# for i in range(len(Pochti_res_mas)):
#   res_mas.append(int(Pochti_res_mas[i]))
# print(sum(res_mas))
# print(max(Towar_s_Uzhe_deistvuushei_skidkoy))
#
import math
f = open('26.1.txt')
s = f.readline()
a = [int(s) for s in f]
a120 = [i for i in a if i > 120]
a120.sort()

sale = math.ceil(sum(a120[:len(a120) // 2]) * 0.25)
print(sum(a) - sale, max(a120[:len(a120) // 2]))












