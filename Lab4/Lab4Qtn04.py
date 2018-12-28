import random

list_integers= list()
for i in range(20):
    list_integers.append(random.randint(1, 10))

keys=list(range(1, 11))
values=list()
for k in keys:
    values.append(list_integers.count(k))

the_dictionary = dict(zip(keys, values))
print(the_dictionary)

# OUTPUT
# {1: 3, 2: 3, 3: 2, 4: 3, 5: 1, 6: 3, 7: 1, 8: 1, 9: 1, 10: 2}   Output changes each time as we have not seeded.
