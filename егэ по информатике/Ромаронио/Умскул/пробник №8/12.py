from typing import Any

mas: list[Any] = []
for n in range(5, 1000):
    s = '8' + '3' * n
    while '83' in s or '233' in s or '3333' in s:
        if '83' in s:
            s = s.replace('83', '3', 1)
        if '233' in s:
            s = s.replace('233', '38', 1)
        if '3333' in s:
            s = s.replace('3333', '2', 1)
