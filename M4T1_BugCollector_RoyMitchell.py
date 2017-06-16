# A program that calculates input of bugs for seven days and displays total.
# 6/16/2017
# CTI-110 M4T1 - Bug Collector
# Roy Mitchell
# Initialize the accumulator.
total_bugs = 0
# Input the number of bugs for each day.
for day in range(1, 8):
    # Prompt user to input bugs collected for the day.
    print('Enter the number of bugs collected on day', day)
    # Input the number of bugs.
    bugs = int(input())
    # Add daily number to total.
    total_bugs = total_bugs + bugs
# Display the total number of bugs collected.
print('You have collected a total of', total_bugs, 'bugs.')
