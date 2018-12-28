from statistics import mean

while True:
    number = int(input("How many students does the Postgraduate program have? (N) \n"))
    if (1<=number<=5):
        break
    else:
        print("Number of students should be between 1 and 5 inclusive. Try again!!")

marks= list()
for i in range(number):
    marks.append(float(input("Enter marks {} \n".format(i+1))))

failing=[mark for mark in marks if mark<50]
passing=[mark for mark in marks if mark>=50]

order=sorted(marks)

print("The average score is ", mean(marks))
print("The lowest mark is ", order[0])
print("The highest mark is ", order[-1])
print("Number of students who have passed is {:1d} and those who failed is {:1d} ".format(len(passing), len(failing)))

# OUTPUT ITEM (a)
# How many students does the Postgraduate program have? (N)
# 1
# Enter marks 1
# 50
# The average score is  50
# The lowest mark is  50
# The highest mark is  50
# Number of students who have passed is 1 and those who failed is 0

# OUTPUT ITEM (b)
# How many students does the Postgraduate program have? (N)
# 2
# Enter marks 1
# 25.5
# Enter marks 2
# 73
# The average score is  49.25
# The lowest mark is  25.5
# The highest mark is  73.0
# Number of students who have passed is 1 and those who failed is 1

# OUTPUT ITEM (c)
# How many students does the Postgraduate program have? (N)
# 3
# Enter marks 1
# 85.5
# Enter marks 2
# 45.5
# Enter marks 3
# 67
# The average score is  66.0
# The lowest mark is  45.5
# The highest mark is  85.5
# Number of students who have passed is 2 and those who failed is 1

# OUTPUT ITEM (d)
# How many students does the Postgraduate program have? (N)
# 4
# Enter marks 1
# 50.5
# Enter marks 2
# 60.5
# Enter marks 3
# 73
# Enter marks 4
# 24.5
# The average score is  52.125
# The lowest mark is  24.5
# The highest mark is  73.0
# Number of students who have passed is 3 and those who failed is 1

# OUTPUT ITEM (e)
# How many students does the Postgraduate program have? (N)
# 5
# Enter marks 1
# 27.5
# Enter marks 2
# 49.5
# Enter marks 3
# 73
# Enter marks 4
# 85.5
# Enter marks 5
# 92.9
# The average score is  65.68
# The lowest mark is  27.5
# The highest mark is  92.9
# Number of students who have passed is 3 and those who failed is 2