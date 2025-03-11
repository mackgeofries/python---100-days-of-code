        # Lesson 32 - Understanding the Offset and Appending Items to Lists

states_of_america = ["Delaware", "Pennsylvania", "etc..."] # creating a list
print(states_of_america) # print out all the items in this list separated by a comma.
                         # in this case it would look like: ['Delaware', 'Pennsylvania', 'etc...']

print(states_of_america[0]) # pull first item from list

states_of_america[1] = "Pencil-vaynia" # ammend just a single item of a list.
print(states_of_america)

states_of_america.append("New State") # add a single additional item to the end of the list
print(states_of_america)              # "a[len(a):] = (x)"

states_of_america.extend(["Canada", "Greenland"]) # able to add multiple new items
print(states_of_america)                          # to the end of the list. Big oof at
                                                  # that joke though...\
                                                  # "a[len(a):] = 'iterable'"
