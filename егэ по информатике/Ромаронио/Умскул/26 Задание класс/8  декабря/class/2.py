f = open('26.2.txt')
n = int(f.readline())
boxes = [int(c) for c in f]
boxes.sort(reverse=True)
polks = []
while boxes:
  gifs = [boxes[0]]
  del boxes[0]
  for box in boxes[:]:
    if gifs[-1] - box >= 5:
      gifs.append(box)
      boxes.remove(box)
  polks.append(gifs)

print(len(polks), len(polks[0]))
print(polks)










