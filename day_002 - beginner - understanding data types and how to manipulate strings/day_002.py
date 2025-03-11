# tip calculator
# Greeting
print("Welcome to the Tip Calculator!")

# get inputs
bill_total = float(input("What is the total price of the bill? "))
tip_option = float(1 + (int(input("How much do you want to tip? 10, 12, 15? ") ) ) / 100)
number_of_people = int(input("How many people are splitting the bill (evenly)? "))

# Do math
per_person = bill_total * tip_option / number_of_people
per_person_rounded = round(per_person, 2)

# output
print(f"Each person should pay ${per_person_rounded:.2f}.")