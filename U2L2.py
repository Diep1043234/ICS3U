import math

x = input("Please input a whole number: ")
x = int(x)
y = input("Please input another nonzero whole number")
y = int(y)
print("Now deciding if", y, "is a factor of", x, "...")
rem = x % y
if rem == 0:
    print("Yes!", y, "is a factor of", x)
