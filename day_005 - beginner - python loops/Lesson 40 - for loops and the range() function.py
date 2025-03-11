
        # Lesson 40 - for loops and the range() function

# for number in range(a, b):    # includes a, but not b. a == start, b == end
#     print(number)

# for number in range(1,10):    # prints numbers from 1 - 10 (not including 10)
#     print(number)

# for number in range(1, 11, 3):  # prints numbers from 1 - 11 (not including 11), counting by 3 
#     print(number)               # range(a, b, c) c == count by #.

# Gauss challenge
# "add up all the numbers from 1 - 100."

# first thought, but not in the spirit of the challenge...
print(sum(range(1,101)))        # using the "b" as 101, because it will count up to there, but not include it
# worked but feels disingenuous...

# second thought
sum_of_numbers = 0
for numbers in range(1,101):    # using the "b" as 101, because it will count up to there, but not include it
    sum_of_numbers += numbers
print(sum_of_numbers)