        # Lesson 56 - Step 3 - Checking if the Player has Won

# Given info:

# import random
# word_list = ["aardvark", "baboon", "camel"]

# chosen_word = random.choice(word_list)
# print(chosen_word)

# placeholder = ""
# word_length = len(chosen_word)
# for position in range(word_length):
#     placeholder += "_"
# print(placeholder)

# # TODO-1: - Use a while loop to let the user guess again.

# guess = input("Guess a letter: ").lower()

# display = ""

# # TODO-2: Change the for loop so that you keep the previous correct letters in display.

# for letter in chosen_word:
#     if letter == guess:
#         display += letter
#     else:
#         display += "_"

# print(display)

import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)
guess = ""


# TODO-1: - Use a while loop to let the user guess again.
while len(guess) < 2:
    underscore_count = len(chosen_word)

    for letter in placeholder:
        if not letter == "_":
            underscore_count -= 1
    
    if underscore_count < 1:
        print("\nYou Win! Congratulations!\n")
        break

    guess = input("Guess a letter: ").lower()
    if len(guess) > 1:
        break

    position = 0
    display = ""

# TODO-2: Change the for loop so that you keep the previous correct letters in display.

    for letter in chosen_word:
        if letter == guess:
            display += letter
        elif not placeholder[position] == "_":
            display += placeholder[position]
        else:
            display += "_"
        
        # print(position)

        position += 1
    print(display)
    placeholder = display
