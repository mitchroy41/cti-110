# This program will read integers from a file and display them.
# 7/6/2017
# CTI-110 M5T1 - File Display
# Roy Mitchell
# Create a loop function to display all integers in the file and close when done.
def main():
    # Open the numbers.text file
    number_file = open('numbers.txt', 'r')
    # Read all the integers in the file.
    for line_of_file in number_file:
        # Convert line string to an integer
        number = int(line_of_file)
        # Display the integer.
        print(number)
    # Close the file.
    number_file.close()
# Call the main function.
main()
