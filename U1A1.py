#Diep
#ICS3U

import math

#Task 1
print("1. Let's calculate the area of a rectangle")
#input length
l = input("Enter its length: ")
l = float (l)
#input width
w = input("Enter its width: ")
w = float(w)
#calculate, round and show the result
print("The area of a rectangle is: ", round(l*w, 2))

#Task 2
print("2. Let's compute the area of a circle")
#input radius
r = input("Enter the radius: ")
r = float (r)
#calculate, round and show the result
print("The area of the circle is: ", round(math.pi*math.pow(r,2), 2))

#Task 3
print("3. Let's compute the surface area and volume of a cylinder")
#input height
h = input("Enter its height: ")
h = float(h)
#input radius
rr = input("Enter its radius: ")
rr= float(rr)
#caculate the surface area
s = (2*math.pi * rr * h) + (2*math.pi*math.pow(rr,2))
#round and show the result
print("The surface area of the cylinder is: ", round(s, 2))
#caculate and show the volume
print("The volumne of the cylinder is: ", round(math.pow(rr,2)*math.pi*h, 2))

#Task 4
print("4. The period is the time it takes for a pendulum to make one back-and-forth swing. It is determined by pendulum length and the force of gravity. Given that acceleration due to gravity is g = 9.8, let's calculate the period based on the length")
#input length
L = input("Enter the length in meters: ")
L = float(L)
#calculate
P = 2*math.pi*math.sqrt(L/9.8)
#round and show the result
print("The period it takes is: ", round(P,2), "seconds.")
