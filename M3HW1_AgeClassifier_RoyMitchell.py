# Create a program that will describe the person based on their age.
# 6/16/2017
# CTI-110 M3HW1 - Age Classifier
# Roy Mitchell
# Input age.
age = int(input('Enter the age of the person in whole years: '))
# Determine if person is an infant and display result.
if age <= 1:
    print('This person is an infant.')
# Determine if person is a child and display result.
else:
    if age < 13:
        print('This person is a child.')
# Determine if person is a teenager and display result.
    else:
        if age < 20:
            print('This person is a teenager.')
# Determine if person is an adult and display result.
        else:
            print('This person is an adult.')
                
