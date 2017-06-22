# This is a program with a loop that asks the user
# to enter a series of positive numbers that are
# added to the total. The loop stops when a negative
# number is entered by the user.
# 6/22/2017
# CTI-110 M4HW1 - Sum of Numbers
# Roy Mitchell
# Identify the accumulator variable.
total = 0
# Get the first positive number.
print('Enter a positive number')
print ('or negative number to end.')
number = int(input('Enter a number: '))
# Add input to total.
while number > 0:
    total = total + number
    # Get the next input number.
    number = int(input('Enter a number: ')) 
# Continue processing as long as input number is positive.   
# Display total and end program when a negative number is entered.
print('Total sum of numbers entered is:', total)
