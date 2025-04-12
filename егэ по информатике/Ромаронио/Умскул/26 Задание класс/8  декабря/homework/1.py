f = open('1.txt')
n = int(f.readline())
boxes = [int(c) for c in f]
gifs = []
boxes.sort(reverse=True)
for box in boxes:
  if gifs == []:
    gifs.append(box)
  elif gifs[-1] - box >= 5:
    gifs.append(box)

print(len(gifs), min(gifs))
