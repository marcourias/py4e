# py4e
This is a set of programs generated as part of the course Python for Everybody by the University of Michingan in Coursera.

## 3.1 - Hourly Pay Calculator with Overtime Calculation

This program prompts the user to input the number of hours worked and their hourly rate of pay. It then converts these inputs from strings to floating-point numbers.

The program checks if the number of hours worked is greater than 40. If so, it calculates the number of extra hours worked and multiplies it by 1.5 times the hourly rate to get the extra pay. The regular hours worked are capped at 40, so any hours worked over 40 are considered extra.

If the number of hours worked is less than or equal to 40, then there are no extra hours worked and no extra pay.

The program then calculates the regular pay by multiplying the number of regular hours worked (40 or less) by the hourly rate. The gross pay is calculated by adding the regular pay and the extra pay (if any).

Finally, the program prints the gross pay to the console.

## 3.2 - Hourly Pay Calculator with Overtime Calculation and Error Handling

This is a Python program that calculates the gross pay for a given number of hours worked at a given hourly rate of pay. It is very similar to the previous program, with the addition of a try-except block to handle input errors.

The program prompts the user to input the number of hours worked and the hourly rate of pay, and stores them in the hrs and rate variables, respectively.

The try-except block attempts to convert the hrs and rate inputs from strings to floating-point numbers using the float() function. If the input is not a valid number, an error will be raised and the except block will execute. In this case, the program prints an error message to the console and exits using the quit() function.

If the input is valid, the program continues to execute as before. It checks if the number of hours worked is greater than 40, calculates any extra pay for hours worked over 40, and calculates the regular pay. Finally, it calculates the gross pay by adding the regular pay and the extra pay (if any), and prints it to the console.

Overall, this program is similar to the previous one, but includes error handling to ensure that the input is valid before attempting the calculations.


## 3.3 

This program is pretty straightforward. It prompts the user to enter a score, converts the input to a float, and then uses a series of if statements to determine the corresponding letter grade. The try-except block is used to catch any input errors that might occur (e.g. if the user enters a string instead of a number).
