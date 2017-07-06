# This program will read random numbers from the random_number.txt file,
# display the numbers individually, display the total quantity of numbers 
# read from the file and display their total.
# 7/6/2017
# CTI-110 M6HW2 - Random Number File Reader
# Roy Mitchell

def main():
    # Open the random_number.txt file for reading.
    read_number = open('random_number.txt', 'r')

    # Initialize an accumluator to 0.
    total = 0

    # Initialize a variable to keep count of quantity
    # of random numbers read from file.
    count = 0

    print ('Below are the random numbers read from the random_number.txt file:')

    # Get random  numbers from file and total them.
    for line in read_number:
        # Convert line to an integer for calculating the total.
        read_number_integer = int(line)
        # Add 1 to the count variable.
        count += 1
        # Display the random number.
        print(read_number_integer)
        # Add value of random number to total variable.)
        total += read_number_integer
        
    # Close the file.
    read_number.close()
    # Display the total quantity of random numbers read.
    print('Quantity of random numbers read from file is:', count)
    # Display the total value of all random numbers read.
    print('Total value of random numbers read from file is:', total)
# Call main function.
main()
    
