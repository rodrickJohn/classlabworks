

while True:
    month = int(input("Enter month number \n"))
    if (1<=month<=12):
        break
    else:
        print("Month value can only be between 1 and 12 inclusive")

if (month == 1):
    print("Month name is January")
    print("Number of days is 31")

elif (month == 2):
    print("Month name is February")
    print("Number of days is either 28 or 29")

elif (month == 3):
    print("Month name is March")
    print("Number of days is 31")

elif (month == 4):
    print("Month name is April")
    print("Number of days is 30")

elif (month == 5):
    print("Month name is May")
    print("Number of days is 31")

elif (month == 6):
    print("Month name is June")
    print("Number of days is 30")

elif (month == 7):
    print("Month name is July")
    print("Number of days is 31")

elif (month == 8):
    print("Month name is August")
    print("Number of days is 31")

elif (month == 9):
    print("Month name is September")
    print("Number of days is 30")

elif (month == 10):
    print("Month name is October")
    print("Number of days is 31")

elif (month == 11):
    print("Month name is November")
    print("Number of days is 30")

elif (month == 12):
    print("Month name is December")
    print("Number of days is 31")

# OUTPUT OF THE PROGRAM FOR MONTH EQUALS 8
# Enter month number
# 8
# Month name is August
# Number of days is 31

# OUTPUT OF THE PROGRAM FOR MONTH EQUALS 2
# Enter month number
# 2
# Month name is February
# Number of days is either 28 or 29

# OUTPUT OF THE PROGRAM FOR MONTH EQUALS TO 13
# Enter month number
# 13
# Month value can only be between 1 and 12 inclusive
# Enter month number