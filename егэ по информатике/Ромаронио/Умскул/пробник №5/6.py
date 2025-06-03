from turtle import *
left(90)
tracer(0)
k = 20
screensize(-5000, 5000)

for i in range(8):
  fd(2 * k)
  left(540)
  back(2 * k)
  right(450)
  forward(5 * k)

pu()
for x in range(-40, 40):
  for y in range(-40, 40):
    goto(x * k, y * k)
    dot(3)
done()
