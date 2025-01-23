from turtle import *
tracer(0)
left(90)
k = 10
x = 4
screensize(5000, 5000)
right(180)
forward(5 * k)
right(90)
forward(50 * k)
right(90)
forward(5 * k)
for _ in range(5):
	seth(90)
	circle(-5 * k, 180)

pu()
for x in range(-100, 40):
	for y in range(-100, 40):
		goto(x * k, y * k)
		dot(3)
done()

s1, s2 = 0, 0
for x in range(1, 1000): 
	s1 += x * (x - 1)
	s2 += 2 * (x + 1) - 1
	if s1 + s2  > 3300000:
		print(x - 1)
		break