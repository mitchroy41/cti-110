# This program converts kilometers to miles.
# 6/30/2017
# CTI-110 M5T1_KilometerConverter
# Roy Mitchell

CONVERSION_FACTOR = 0.6214

def main():
    # Get the number of kilometers from user.
    print('Convert kilometers to miles.')
    kilometers = float(input('Enter the number of kilometers: '))
    # Convert kilometers to miles and show result.
    display_miles(kilometers)
                     
# This function converts kilometers to miles.
def display_miles(km):
    miles = km * CONVERSION_FACTOR
    print(km, 'kilometers equals', format(miles, '.2f'),'miles.')
    
# Call the main function.
main()
