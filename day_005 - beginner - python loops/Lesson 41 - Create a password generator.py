
        # Lesson 41 - Create a password generator

# given information
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Easy Level
password = ""
for number in range(1,nr_letters+1):
    password += random.choice(letters)

for number in range(1, nr_numbers+1):
    password += random.choice(numbers)

for number in range(1, nr_symbols+1):
    password += random.choice(symbols)

print(password)     # this does not perfectly match up with demonstration, as I switched it to do letters,
                    # numbers, symbols - rather than letters, symbols, numbers.

# Hard Level
password_hard = ""

# doing something like a while loop, then creating a sum of the total characters, and only reducing when
# it adds a character, seems like the best option, but that's outside the scope here...
#
# while total_number is greater than 0... 
# pick a random stack to choose from.
#   while that stack (from nr_numbers or whatever) is greater than 0..
#   add that character to the list, then
#   -1 to both nr_numbers (or whichever) and total_number
# loop until total_number is 0

total = nr_letters + nr_numbers + nr_symbols
nr_choices = [nr_letters, nr_numbers, nr_symbols]
options = [letters, numbers, symbols]

for number in range(1, total+1):

    if nr_choices[0] > 0:
        if nr_choices[1] > 0:
            if nr_choices[2] > 0:
                randpick = random.randint(0,2)
                password_hard += random.choice(options[randpick])
                nr_choices[randpick] -= 1
            else:
                randpick = random.randint(0,1)
                password_hard += random.choice(options[randpick])
                nr_choices[randpick] -= 1
        else:
            if nr_choices[2] > 0:
                randpick = random.randint(0,1) *2
                password_hard += random.choice(options[randpick])
                nr_choices[randpick] -= 1
            else:
                randpick = 0
                password_hard += random.choice(options[randpick])
                nr_choices[randpick] -= 1
    else:
        if nr_choices[1] > 0:
            if nr_choices[2] < 0:
                randpick = random.randint(0,1) + 1
                password_hard += random.choice(options[randpick])
                nr_choices[randpick] -= 1
            else:
                randpick = 1
                password_hard += random.choice(options[randpick])
                nr_choices[randpick] -= 1
        else:
            randpick = 2
            password_hard += random.choice(options[randpick])
            nr_choices[randpick] -= 1
        
print(password_hard)

# I didn't WANT to do nested ifs, and I'm sure there's a much better option, but.. it works.
# I struggled for a while with this, because I had "nr_choices < 0" instead of "nr_choices > 0".
# *sigh*. Oh well, I figured it out.