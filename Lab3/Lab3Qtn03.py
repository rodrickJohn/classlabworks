
while True:
    input_data = input("Enter five-digit integer \n")  #input function returns a string
    if (len(input_data))==5:
        break
    else:
        print("The integer must have five digits")

if (input_data == input_data[::-1]):
    print("Entered number is palindrome")
else:
    print("Entered number is not a palindrome")


# OUTPUT FOR INPUT 12321
# Enter five-digit integer
# 12321
# Entered number is palindrome

# OUTPUT FOR INPUT 12345
# Enter five-digit integer
# 12345
# Entered number is not a palindrome

# OUTPUT FOR INPUT 435
# Enter five-digit integer
# 435
# The integer must have five digits
# Enter five-digit integer