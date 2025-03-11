# ***********
# pizza pricing
# ***********

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")

# todo: work out how much they need to pay based on their size choice.

# todo: work out how much to add to their bill based on their pepperoni choice

# todo: work out how much their final amount based on whether if they want extra cheese

# S - $15
# M - $20
# L - 25
# add pepperoni for small pizza (Y or N): +$2
# add pepperoni for M or L pizza (Y or N): +$3
# add exttra cheese for any size pizza: +$1
# print out "Your final bill is: $XX" based on choices.

print("\nWelcome to Python Pizza Deliveries!\n")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
total = 0
valid_choices = True
size = size.upper()
pepperoni = pepperoni.upper()
extra_cheese = extra_cheese.upper()

if extra_cheese == "Y":
    total += 1
elif extra_cheese == "N":
    total += 0
else:
    print("Invalid Cheese Choice")
    valid_choices = False

if size == "S":
    total += 15
elif size == "M":
    total += 20
elif size == "L":
    total += 25
else:
    print("Invalid Pizza Size")
    valid_choices = False


if pepperoni == "Y":
    if size == "S":
        total += 2
    else:
        total += 3
elif pepperoni == "N":
    total += 0
else:
    print("Invalid Pepperoni Choice")
    valid_choices = False

if valid_choices == True:
    print(f"\nYour total comes to ${total}.\n")