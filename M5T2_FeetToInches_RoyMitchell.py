# This program converts feet to inches.
# 6/30/2017
# CTI-110 M5T2_FeetToInches
# Roy Mitchell

# Constant to determine inches per foot.
INCHES_PER_FOOT = 12

def main():
    # Get the number of feet from user.
    print('Convert feet to inches.')
    feet = int(input('Enter the number of feet: '))
    # Convert feet to inches and show result.
    print(feet, 'feet equals', feet_to_inches(feet),'inches.')
                     
# This function converts feet to inches.
def feet_to_inches(ft):
    return ft * INCHES_PER_FOOT
   
# Call the main function.
main()
