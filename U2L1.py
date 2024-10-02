print("Make a choice from the following menu: ")
print("A: apples")
print("B: bananas")
print("C: cherries")

ch = input("Your choice: ")

if (ch == "A"):
    print("I prefer apples")
elif (ch == "B"):
    print("I prefer bananas")
else:
    print("I prefer cherries")
#any erroneous input results prints out I prefer cherries

#Modify 1
print("Make a choice from the following menu: ")
print("A: apples")
print("B: bananas")
print("C: cherries")

ch = input("Your choice: ")

if (ch == "A" or "a"):
    print("I prefer apples")
elif (ch == "B" or "b"):
    print("I prefer bananas")
elif(ch == "C" or "c"):
    print("I prefer cherries")
else:
    print("Please run the program again and enter only A, B or C")

#Modify 2
#ask user to input a number
x = float(input("Enter a number from 1 - 100: "))

#first compound condition
if (x >= 80) and (x <= 100):
  print("A")
#second compound condition
elif (x >= 70) and (x <= 79):
  print("B")
#third compound condition
elif (x >= 60) and (x <= 69):
  print("C")
#fourth compound condition
elif (x >= 50) and (x <= 59):
  print("D")
#fifth compound condition
elif (x < 50):
  print("F")
else:
  print("Input is invalid. Please try again.")
