        # Lesson 48 - Hurdles Challenge using While Loops

'''
Reeborg has entered a hurdle race. Make him run the course, following the path shown.

The position and number of hurdles changes each time this world is reloaded.
What you need to know
The functions move() and turn_left().
The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.
How to use a while loop and an if statement.
Your program should also be valid for worlds Hurdles 1 and Hurdles 2.

https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
'''

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()

# I thought I was being clever before doing move_left and move_right, to eliminate the extra move()
# calls, but it turned out to be detrimental. So, back to the original-ish way of doing it.