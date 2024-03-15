"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.

numChars = input("Enter the number of Characters: ")
color = input("Enter the color: ")
woodType = input("Enter the type of wood: ")

if not numChars.isdigit():
  print("Invalid number of characters.")

if not color.isalpha():
  print("Invalid color.")

if not woodType.isalpha():
  print("Invalid wood type.")

# Charge for this sign.
charge = 35
# Number of characters.
if float(numChars) > 5:
  charge += (float(numChars) - 5) * 4
# Color of characters.
if color == "gold":
  charge += 15
# Type of wood.
if woodType == "oak":
  charge += 20
# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))