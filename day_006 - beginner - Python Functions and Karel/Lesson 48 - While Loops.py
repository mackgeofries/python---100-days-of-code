        # Lesson 48 - While Loops

# while something_is_true:
#     do_the_thing_repeatedly
#     until_it's no longer true

'''
Reeborg has entered a hurdle race, but he does not know in advance how long the race is. Make him run the course, following a path similar to the one shown, but stopping at the only flag that will be shown after the race has started.
What you need to know
The functions move() and turn_left().
The condition at_goal() and its negation.
How to use a while loop.
Your program should also be valid for world Hurdles 1.

https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
'''

def move_right():
    move()
    turn_left()
    turn_left()
    turn_left()

def move_left():
    move()
    turn_left()
    
def jump():
    move_left()
    move_right()
    move_right()
    move_left()

while not at_goal():
    jump()

# can create an infinite loop, ***be careful***!