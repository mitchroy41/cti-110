# Calculate the projected Total Sales
# 6/5/2017
# CTI-110 M2T1 - Sales Prediction
# Roy Mitchell
# Input Total Sales.
total_sales=float(input('Enter the projected sales: '))
# Calculate the profit as 23 percent of total sales.
profit=total_sales*.23
# Display the profit.
print('The profit is $',format(profit, ',.2f'))
