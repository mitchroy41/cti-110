# Compare rectangle areas
# 6/16/2017
# CTI-110 M3T1 - Areas of Rectangles
# Roy Mitchell
# This program will determine which rectangle has the greatest area.
# Get length and width of rectangle 1.
length1 = int(input('What is the length of rectangle 1?: '))
width1 = int(input('What is the width of rectangle 1?: '))
# Get length and width of rectangle 2.
length2 = int(input('What is the length of rectangle 2?: '))
width2 = int(input('What is the width of rectangle 2?: '))            
# Calculate the area of rectangle 1.
area1 = length1 * width1
# Calculate the area of rectangle 2.
area2 = length2 * width2
# Determine which rectangle has the greatest area and display result.
if area1 > area2:
             print('Rectangle 1 has the greatest area.')
elif area1 < area2: 
             print('Rectangle 2 has the greatest area.')
else:
             print('Both rectangles have the same area.')
