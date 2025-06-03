# f = open('26.txt')
# m = f.readline()
# mas = [0 for i in range(1, 50401)]
# buff = 0
# for s in f:
#     start, end = map(int, s.split())
#     for i in range(50401):
#         if start == i:
#             buff += 1
#             mas[i] = buff
#         if end == i:
#             buff -= 1
#             mas[i] = buff
#
# k = 0
# print(max(mas))
# for i in mas:
#     if i == 4793:
#         k += 1
# print(k)

f = open("26.txt")
n = int(f.readline())
time_start, time_end = 8 * 60 * 60, 14 * 60 * 60
process = [0] * 86401

for i in range(n):
    start, end = map(int, f.readline().split())
    process[start] += 1
    process[end] -= 1

print(process)

current_process = max_process = max_length = 0
for second in range(len(process)):
    current_process += process[second]
    if time_start <= second <= time_end:
        if current_process > max_process:
            max_process = current_process
            max_length = 1
        elif current_process == max_process:
            max_length += 1

print(max_process, max_length)

