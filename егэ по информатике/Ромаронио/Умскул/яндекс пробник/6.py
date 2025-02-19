from turtle import *
left(90)
tracer(0)
k = 20
screensize(5000, 5000)
for _ in range(36):
  forward(4 * k)
  right(90)
pu()
forward(4 * k)
right(90)
pd()
for _ in range(8):
  forward(6 * k)
  right(90)
pu()
for x in range(-40, 40):
  for y in range(-40,40):
    goto(x * k, y * k)
    dot(3)
done()