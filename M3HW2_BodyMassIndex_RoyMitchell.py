# This program calculates a person's BMI.
# 6/16/2017
# CTI-110 M3HW2 - Body Mass Index
# Roy Mitchell
# Get person's height and weight.
height = float(input('Enter your height in inches: '))
weight = float(input('Enter your weight in lbs: '))
# Calculate BMI.
bmi = weight * 703/height**2
# Display calculated BMI.
print('Your BMI is:', format(bmi, '.2f'))
# Determine if BMI is optimal, underweight or overweight and display result.
if bmi < 18.5:
    print('You are underweight.')
elif bmi <= 25:
    print('You are of optimal weight.')
elif bmi > 25:
    print('You are overweight.')
