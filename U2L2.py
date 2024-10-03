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
x = input("Please input a whole number between 1 and 20: ")
x = int(x)
if (x<1 or x>20):
  print("%d is outside of range. Cannot continue." %x) #the condition wont execute if x is outside of range
else:
  y = input("Please input another whole number between 1 and 20: ")
  y = int(y)
  if (y<1 or y>20):
    print("%d is outside of range. Cannot continue." %y) #the condition wont execute if y is outside of range
  else:
    print("Now deciding if", y, "is a factor of", x, "...")
  rem = x % y
  if rem == 0:
    print("Yes!", y, "is a factor of", x) 
  else: 
    print(y, "is not a factor of ", x)
