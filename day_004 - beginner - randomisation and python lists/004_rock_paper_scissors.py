        # Lesson 35 - Rock Paper Scissors challenge

import random

# paper = "\n    _______\n---'   ____)____\n          ______)\n          _______)\n         _______)\n---.__________)"
# rock = "\n    _______\n---'   ____)\n      (_____)\n      (_____)\n      (____)\n---.__(___)"
# scissors = "\n    _______\n---'   ____)____\n          ______)\n       __________)\n      (____)\n---.__(___)"

# rps -> rock paper scissors
rps = ["\n    _______\n---'   ____)\n      (_____)\n      (_____)\n      (____)\n---.__(___)",  "\n    _______\n---'   ____)____\n          ______)\n          _______)\n         _______)\n---.__________)",  "\n    _______\n---'   ____)____\n          ______)\n       __________)\n      (____)\n---.__(___)"]

player_choice = int(input("What will you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n "))
computer_choice = random.randint(0,2)

print(rps[player_choice])
print("\nComputer chose:")
print(rps[computer_choice])

# 0 beats 1, 1 beats 2, 2 beats 0

if player_choice == 1:
    if computer_choice == 1:
        print("\nIt's a draw")
    elif computer_choice == 0:
        print("\nYou win")
    elif computer_choice == 2:
        print("\nYou lose")
elif player_choice == 2:
    if computer_choice == 2:
        print("\nIt's a draw")
    elif computer_choice == 1:
        print("\nYou win")
    elif computer_choice == 0:
        print("\nYou lose")
elif player_choice == 0:
    if computer_choice == 0:
        print("\nIt's a draw")
    elif computer_choice == 2:
        print("\nYou win")
    elif computer_choice == 1:
        print("\nYou lose")

# I forgot about block notes, which would have made it a lot more obvious which one was which.
# so, for example...
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# etc...
#
# and then doing...
# rps = [rock, paper, scissors].
# and (I think) continuing on from there.