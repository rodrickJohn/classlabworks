
while True:
    w = float(input("Enter weight in kg \n"))
    h = float(input("Enter height in meters \n"))
    if (w>0 or h>0):
        break
    else:
        print("Height and Weight cannot be zero or negative")

BMI = w/(h**2)  #in the original question there was a 't' that has not been defined. was it an error?

if (BMI<18.5):
    interpretation= "Underweight"
elif (18.5 <= BMI < 25.0):
    interpretation="Normal"
elif (25.0 <= BMI < 30.0):
    interpretation="Overweight"
elif (BMI >= 30.0):
    interpretation="Obese"

print("For a person with weight {:.2f} kg and height {:.2f} meters BMI is {:.2f} and BMI interpretation is {}".format(w,h,BMI,interpretation))
