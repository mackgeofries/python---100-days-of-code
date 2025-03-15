        # Lesson 62 - Positional vs Keyword Arguments

# functions with more than one input

def greet_with(name, location):
    # goal:
    # print "Hello <name>"
    # print "What is it like in <location>"
    print(f"Hello {name}.")
    print(f"What is it like in {location}?")
    

greet_with("Doctor", "the Tardis")

# "what happens if you switch the arguments that you pass in?
# greet_with("the Tardis", "Doctor")
#
# It should print out "Hello the Tardis.", "What is it like in Doctor?"
#
### this is known as a POSITIONAL ARGUMENT ###
### the other option is KEYWORD ARGUMENTS ###
# this is done with "my_function(parameter1 = variable_x, parameter2 = variable_y)"
# but can be done in any order. So if you wanted to put parameter2 first, then
# you could do "my_function(parameter2 = variable_y, parameter1 = variable_x)"

greet_with(location="The Enterprise", name="Jean Luc")

