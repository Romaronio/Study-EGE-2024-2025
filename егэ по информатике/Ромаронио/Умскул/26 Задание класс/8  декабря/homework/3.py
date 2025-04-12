f = open('3.txt')
n = int(f.readline())
polk = []
boxes = []
for s in f:
  length, color = s.split()
  boxes.append([int(length), color])

boxes.sort(reverse=True)

while boxes:
  gifs = [boxes[0]]
  del boxes[0]
  for box in boxes[:]:
    if gifs[-1][0] - box[0] >= 8 and gifs[-1][1] != box[1]:
      gifs.append(box)
      boxes.remove(box)
  polk.append(gifs)

print(len(polk), len(polk[0]))
