import math
length = input("Please input a length: ")
length = float(length)
area = math.pow(length, 2)
print("The area of a square of side length", length, "is:", round(area,2))


r= input("Enter the circle's radius: ")
r = float(r)

#The length of the side of the square is the circle's diameter so it's 2r
#area of the square 
area2 = math.pow((2*r),2)

#area of the semicircle
area3 = 0.5*math.pi*r*2

#area of the Norman Window shape:
area4 = area2 + area3
print("Area of the Norman Window shape is: ", round(area4,2))
