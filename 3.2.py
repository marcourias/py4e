hrs = input("Enter Hours:")
rate = input("Enter Rate: ")


try:
    h = float(hrs)
    rate = float(rate)
except:
    print("Ingrese un número válido.")
    quit()

if h > 40:
    extra_hours = h - 40
    extra_pay = extra_hours * rate * 1.5
    h = 40
else:
    extra_pay = 0
    
regular_pay = h * rate
gross_pay = regular_pay + extra_pay

print(gross_pay)
