hrs = input("Enter Hours:")
rate = input("Enter Rate: ")

h = float(hrs)
rate = float(rate)


if h > 40:
    extra_hours = h - 40
    extra_pay = extra_hours * rate * 1.5
    h = 40
else:
    extra_pay = 0
    
regular_pay = h * rate
gross_pay = regular_pay + extra_pay

print(gross_pay)
