        # Lesson 63 - Caesar Cipher Part 1 - Encryption

# Given information:
''' alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))


# # TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# # TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
# #  by the shift amount and print the encrypted text.

# # TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# # TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
# #  message.'''

### ATTEMPT 1 ###
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# # TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
# def encrypt(original_text, shift_amount):
#     encrypted_text = ""
#     for letter in original_text:
#         letter_position = 0
#         for position in alphabet:
#             if letter == position:
#                 if letter_position + shift_amount > 25:
#                     letter_position -= 26
#                 encrypted_text += alphabet[letter_position + shift_amount]
#                 break
#             else:
#                 letter_position += 1
#     print(f"Here is the encoded result: {encrypted_text}")

# # TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
# #  by the shift amount and print the encrypted text.

# # TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# # TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
# #  message.

# encrypt(text, shift)

# probably not the most elegant way of doing this..
# seems to work though.

# watching more of the training, I've learned of .index(). This seems to solve most of the code I wrote.

### ATTEMPT 2 ###
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text, shift_amount):
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
    encrypted_text = ""
    for letter in original_text:
        if alphabet.index(letter) + shift_amount < 25:
            encrypted_text += alphabet[alphabet.index(letter) + shift_amount]
        else:
            encrypted_text += alphabet[alphabet.index(letter) + shift_amount - 26]
    print(f"Here is the encoded result: {encrypted_text}")
# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

encrypt(text, shift)

# wow. much more better-er. Oh well...