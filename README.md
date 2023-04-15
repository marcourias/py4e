# py4e
This is a set of programs generated as part of the course Python for Everybody by the University of Michingan in Coursera.

## 3.1 - Hourly Pay Calculator with Overtime Calculation

This program prompts the user to input the number of hours worked and their hourly rate of pay. It then converts these inputs from strings to floating-point numbers.

The program checks if the number of hours worked is greater than 40. If so, it calculates the number of extra hours worked and multiplies it by 1.5 times the hourly rate to get the extra pay. The regular hours worked are capped at 40, so any hours worked over 40 are considered extra.

If the number of hours worked is less than or equal to 40, then there are no extra hours worked and no extra pay.

The program then calculates the regular pay by multiplying the number of regular hours worked (40 or less) by the hourly rate. The gross pay is calculated by adding the regular pay and the extra pay (if any).

Finally, the program prints the gross pay to the console.
