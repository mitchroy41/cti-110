# This program writes user specified quantity of random numbers to a file in a range from 1 through 500.
# 7/6/2017
# CTI-110 M6HW1 - Random Number File Writer
# Roy Mitchell

import random
def main():
    # Have user specify the quantity of random numbers that will be saved to file.
    quantity_num = int(input('How many random numbers do you want to save to file? '))

    # Create and open a file to hold the random numbers.
    num_file = open('random_number.txt', 'w')

    # Get random number from 1 to 500 based on user specified quanity to input.
    for count in range(1, quantity_num + 1):
        number = random.randint(1, 500)
        # Convert random number to string and write to file.
        num_file.write(str(number) + '\n')
        # Display random number that was saved to file.
        print(number)
    # Close the file.
    num_file.close()
    print('All of the random numbers have been created and saved to the random_number.txt file.')
# Call the main function.
main()
