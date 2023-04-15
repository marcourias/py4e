# Prompt the user to input hours worked and hourly rate
hrs = input("Enter Hours:")
rate = input("Enter Rate: ")

# Convert inputs to float
h = float(hrs)
rate = float(rate)

# Calculate regular pay and extra pay (if any) for hours worked over 40
if h > 40:
    extra_hours = h - 40
    extra_pay = extra_hours * rate * 1.5
    h = 40
else:
    extra_pay = 0
    
regular_pay = h * rate

# Calculate gross pay by adding regular pay and extra pay
gross_pay = regular_pay + extra_pay

# Print the gross pay to the console
print(gross_pay)
