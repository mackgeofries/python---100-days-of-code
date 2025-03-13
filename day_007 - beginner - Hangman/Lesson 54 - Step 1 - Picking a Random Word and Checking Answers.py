        # Lesson 54 - Step 1 - Picking a Random Word and Checking Answers

# Given things:
# word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "right" if it is, "wrong" if it's not.


### MY ANSWER ###
# import random

# word_list = ["aardvark", "baboon", "camel"]

# chosen_word = random.choice(word_list)
# chosen_word_list = list(chosen_word)
# print(chosen_word)

# guess = input("Guess a letter: ").lower()
# guess_correct = False         # getting ahead of myself maybe...

# for num in range(len(chosen_word_list)):
#     # print(chosen_word_list[num])
#     if guess == chosen_word_list[num]:
#         # guess_correct = True  # getting ahead of myself maybe...
#         print("Right")
#     else:
#         print("Wrong")


### GIVEN SOLUTION ###
import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Guess a letter: ").lower()

for letter in chosen_word:      # for whatever reason, when I tried this on my own, it threw errors, 
    if letter == guess:         # but now it does it fine. idk... this seems like obviously the 
        print("Right")          # better solution. for now at least.
    else:
        print("Wrong")

# if guess_correct == True:
#     print("Right")
# else:
#     print("Wrong")
    