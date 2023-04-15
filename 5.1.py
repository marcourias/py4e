# Exercise 1: Write a program which repeatedly reads numbers until the user enters "done". 
# Once "done" is entered, print out the total, count, and average of the numbers. 
# If the user enters anything other than a number, detect their mistake using try and except
# and print an error message and skip to the next number.

sum = 0
i = 0

while True:
    i += 1
    num = input("Enter a number: ")
    
    if num == "done":
        break
    else:
        try:
            sum += int(num)
        except:
            print("Invalid number")


avg = sum/i
    
print(f"The sum is: {sum}\nThe count is: {i}\nThe average is: {avg}")
