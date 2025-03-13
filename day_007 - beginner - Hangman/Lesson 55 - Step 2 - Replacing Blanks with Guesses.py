        # Lesson 55 - Step 2 - Replacing Blanks with Guesses

# given info:

# import random
# word_list = ["aardvark", "baboon", "camel"]

# chosen_word = random.choice(word_list)
# print(chosen_word)

# # TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word

# guess = input("Guess a letter: ").lower()

# # TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.

# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")

import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word

placeholder = ""

for letter in chosen_word:
    placeholder += "_"
print(placeholder)

guess = input("Guess a letter: ").lower()


# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
# position = 0
placeholder = ""
for letter in chosen_word:
    # print(chosen_word[position])
    if letter == guess:
        placeholder += letter
    else:
        placeholder += "_"
    # position += 1
print(placeholder)