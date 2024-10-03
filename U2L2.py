import math

x = input("Please input a whole number: ")
x = int(x)
y = input("Please input another nonzero whole number")
y = int(y)
print("Now deciding if", y, "is a factor of", x, "...")
rem = x % y
if rem == 0:
    print("Yes!", y, "is a factor of", x)


#modify 
elif:
  y = input("Please input another whole number between 1 and 20: ")
  y = int(y)
  if (y<1 and y>20):
    print("%d is outside of range. Cannot continue." %y)
  else:
    print("Now deciding if", y, "is a factor of", x, "...")
  rem = x % y
  if rem == 0:
    print("Yes!", y, "is a factor of", x)
