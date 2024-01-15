#Carlton Austin Jr
#Welcome to the Python Tutorial - Working with Numbers
#1st input for entering user's name
name=input("Please enter your name: ")

#Program to user intro
print(f"Nice to meet you {name}!\nLet's discuss 4 basic math equations:\n"
      f"Addition +\nSubtraction -\nMultiplication x\nDivision /\n")

#select 2 numbers via input
num1 = int(input("Choose your 1st number: "))
num2 = int(input("Choose your 2nd number: "))

#display the calculations for each of the equations
print(f"Addition:{num1 + num2}\nSubtract:{num1 - num2}\nMultiplication:{num1 * num2}\nDivision:{num1/num2}")

#Extra tip fot the road
print("Tip: Use 'sum(value1,value2,etc.)' in the same way as '+' for cleaner code when adding multiple items.")