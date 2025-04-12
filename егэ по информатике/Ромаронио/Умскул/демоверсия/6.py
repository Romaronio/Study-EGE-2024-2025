from turtle import *
left(90)
tracer(0)
screensize(5000, 5000)
k = 20

for _ in range(10):
  forward(22 * k)
  right(90)
  forward(6 * k)
  right(90)

pu()
forward(1 * k)
right(90)
forward(5 * k)
left(90)
pd()

for _ in range(9):
  forward(53 * k)
  right(90)
  forward(75 * k)
  right(90)

pu()
for x in range(-40, 40):
  for y in range(-40, 40):
    setpos(x * k, y * k)
    dot(3)

done()