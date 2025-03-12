        # Lesson 50 - Final Project - Escaping the Maze

'''
Reeborg was exploring a dark maze and the battery in its flashlight ran out.

Write a program using an if/elif/else statement so Reeborg can find the exit. The secret is to have Reeborg follow along the right edge of the maze, turning right if it can, going straight ahead if it can’t turn right, or turning left as a last resort.

What you need to know
The functions move() and turn_left().
Either the test front_is_clear() or wall_in_front(), right_is_clear() or wall_on_right(), and at_goal().
How to use a while loop and if/elif/else statements.
It might be useful to know how to use the negation of a test (not in Python).

https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
'''

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()
    else:
        turn_right()
        move()

# hmm, the exact same solution from lesson 49 worked for this too.
# Oh! There's a more challenging challenge!

# Problem_world and problem_world2:
# robot gets stuck in an infinite loop because it's set up to automatically turn left if 
# there's not a wall to the right.
# problem_world3 I didn't haven a problem with at all, so I'm not sure what it was supposed to do.

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while right_is_clear():
    if front_is_clear():
        move()
    else:
        turn_right()
    
while not at_goal():
    if wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()
    else:
        turn_right()
        move()
