from turtle import *
tracer(0)
left(90)
k = 30
x = 5
screensize(5000, 5000)
forward(3 * k)
while x:
	for _ in range(2):
		forward(x * k)
		right(90)
	forward(x * k)
	left(90)
	forward(1 * k)
	left(90)
	x -= 1
back(3 * k)	

pu()
for x in range(-40, 40):
	for y in range(-40, 40):
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