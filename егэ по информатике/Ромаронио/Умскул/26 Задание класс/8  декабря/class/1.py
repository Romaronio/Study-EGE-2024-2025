f = open('26.1.txt')
n = int(f.readline())
boxes = [int(c) for c in f]
boxes.sort(reverse=True)
gift = []
for box in boxes:
  if gift == []:
    gift.append(box)
  elif gift[-1] - box >= 3:
    gift.append(box)

print(len(gift), min(gift))

