# Calculating a grade, debug the code.
# 6/16/2017
# CTI-110 M3T2 - Debugging
# Roy Mitchell
# This exercise requires correction of indentations written in the code and
# requires altering of the code for it to run correctly.
# Establish variables to represent the grade thresholds.
A_score = 90
B_score = 80
C_score = 70
D_score = 60
# Have user input a test score.
score = int(input('Enter your test score: '))
# Determine a grade based on test score inputted.
if score >= A_score:
    print('Your grade is A.')
else:
    if score >= B_score:
        print('Your grade is B.')
    else:
        if score >= C_score:
            print('Your grade is C.')
        else:
            if score >= D_score:
                print('Your grade is D.')
            else:
                print('Your grade is F.')
                
