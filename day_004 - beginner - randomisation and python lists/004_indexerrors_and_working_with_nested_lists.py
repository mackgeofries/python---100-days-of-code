        # Lesson 34 - IndexErrors and Working with Nested Lists

# indexerrors

# states_of_america = ["Delaware", "Pennsylvania", "etc..."] 

# print(len(states_of_america)) 
#     # returns "3", so what happens if we do...
#     # print(states_of_america[3])
#     # IndexError: list index out of range.
#     # because there are 3 items in the list, but starting at 0, to get the last item
#     # it should be...
# print(states_of_america[2])
#     # or print(states_of_america[len(states_of_america)-1])

            # **********************

# nested lists

# starting info
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"] # I know tomatoes are technically a fruit, but I'm just writing what's given...

dirty_dozen = [fruits, vegetables]
print(dirty_dozen) # shows nested lists, the list with two items called "dirty_dozen" containing "fruits" and "vegetables",
                   # as well as what each of those respective lists have within them.
                   # [['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears'], ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']]

print(dirty_dozen[1]) # prints: ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']
print(dirty_dozen[1][1]) # prints: Kale

    # this shows that with a nested list, the first [] is for the top level list (fruits, vegetables), and the second [] is for the 
    # individual items within the first selected list ("Spinach", "Kale", "Tomatoes", "Celery", "Potatoes").
