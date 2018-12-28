# solution for question 1 (c) i

import statistics

scores = list()
fhandle = open('lab5Qtn1Values.txt', 'r')   # this returns a string of values ending with \n

for score in fhandle:
    scores.append(int(score.rstrip()))    # type-cast string scores to int since randbetween returns integers

print("The minimum score is {:1d}".format(min(scores)))
print("The maximum score is {:1d}".format(max(scores)))
print("The average score is {:.2f}".format(statistics.mean(scores)))
print("The stdev score is {:.2f}".format(statistics.stdev(scores)))

# output

# The minimum score is 1
# The maximum score is 100
# The average score is 54.24
# The stdev score is 30.68

# responding to question 1 (c) ii ...
# comparing the output in this program with the answers in the LabQtn1Values.xlsx they are all exactly equal to 2 d.p