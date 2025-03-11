        # Lesson 31 - Random Module
       
    # importing things
# import random
    # saved in same folder, my_module.py
# import my_module
 
    # my_module (from my file my_module.py) .my_fav_number (my variable from that file)
# print(my_module.my_fav_number)
 
    # random whole number between "a" and "b". a <= x <= b.
    # random.randint(a,b)
# print(random.randint(1, 10))
 
    # random floating point number. 0 <= x < 1
# print(random.random())
 
    # random float number a <= x <= b (in theory, but maybe not equal to either. depends on rounding)
# print(random.uniform(1,10))
 
    # objective: create a heads or tails app.
   
# *************
   
    # generating random number, then rounding it to the nearest whole number to give either
    # a heads or tails.
    #
    # could have also done random.randint(0,1) for same result, I think...
coin_flip = round(random.random())
 
if coin_flip == 0:
    print("Heads!")
else:
    print("Tails!")