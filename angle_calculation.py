import math

distance = float(input("How far? (use meters) "))
#print(distance)
#Height in meters
height = 7.0
#Initial velocity in meters/sec
initial_velocity = 600
angle = None
g = -9.8
p0 = initial_velocity**2
p1 = 2*(p0-g*height)
print p1
p2 = 2*(g**2)*(distance**2 + height**2)
print p2
p3 = g*distance
print p3

if(p1>p2):
	p4_1 = (p0 + math.sqrt(p1-p2))/p3
	p4_2 = (p0 - math.sqrt(p1-p2))/p3
	
	theta_1 = math.atan(p4_1)
	theta_2 = math.atan(p4_2)

	print("Theta 1 is: " + str(theta_1))
	print("Theta 2 is: " + str(theta_2))
else:
	print("Error")
	

