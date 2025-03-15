        # Lesson 61 - Functions with Inputs

# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("Hello World!")
    print("Second Print Statement")
    print("3")

greet()

# passing in a variable:
# def my_function(something):       # pass in whatever data, and it gets stored in the 
#     do this with something        # variable "something" then you can use it within the function.
#     then this
#     finally this.
#
# my_function("Hello")
# my_function(123)                  # different options...
# my_function(variable_name)

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"My name is {name} too!")
    print("That's so crazy!")

greet_with_name(input("What's your name? "))

# in this example...
# "name" (the variable being created) is the "PARAMETER"
# and the actual data being passed in (your name)
# is the "ARGUMENT".