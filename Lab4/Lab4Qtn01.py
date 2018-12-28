import random
import statistics

scores= list()      # initializing scores as an empty list object
for i in range(100):
    scores.append(round(random.uniform(0, 100), 1))   # marks are float numbers that lie between 0 and 100 inclusive

average= sum(scores)/len(scores)     # sum the list divide by length of the list

failing = [score for score in scores if score < 50]
passing = [score for score in scores if score >= 50]
A = [score for score in scores if score >= 70]
Bplus = [score for score in scores if ((score >= 60) and (score < 70))]
B = [score for score in scores if ((score >= 50) and (score < 60))]
C = [score for score in scores if ((score >= 40) and (score < 50))]
D = [score for score in scores if ((score >= 35) and (score < 40))]
E = [score for score in scores if ((score >= 0) and (score < 35))]

print("The lowest mark is {:.1f}".format(min(scores)))    # in response to Qn1 (a)
print("The highest mark is {:.1f}".format(max(scores)))    # in response to Qn1 (a)
print("The average mark calculated without using the math module is {:.2f}".format(average))    # in response to Qn1 (a)
print("The average mark calculated using the statistics module is {:.2f}".format(statistics.mean(scores)))  # to Qn1 (b)
print("The stdev mark calculated using the statistics module is {:.2f}".format(statistics.stdev(scores)))  # to Qn1 (b)
print("Number of students who have passed is {:1d} and those who failed is {:1d} ".format(len(passing), len(failing)))

print("Grade", "No. of students")
print('A     ', len(A))
print('B+     ', len(Bplus))
print('B     ', len(B))
print('C     ', len(C))
print('D     ', len(D))
print('E     ', len(E))


# OUTPUT
# The lowest mark is 0.1
# The highest mark is 97.0
# The average mark calculated without using the math module is 46.72
# The average mark calculated using the statistics module is 46.72
# The stdev mark calculated using the statistics module is 28.49
# Number of students who have passed is 51 and those who failed is 49
# Grade No. of students
# A      24
# B+      11
# B      16
# C      8
# D      3
# E      38