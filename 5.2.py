# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message
#  and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below. 

smallest =  None
largest = None


while True:
    text = input('Enter your number: ')
    
    if text == 'done':
        break

    try:
        num = int(text)
    except:
        print('Invalid input')
        continue

    if largest == None:
        largest = num
    elif num > largest:
        largest = num
    
    if smallest == None:
        smallest = num
    elif num < smallest:
        smallest = num


print(f'Maximum is {largest}\nMinimum is {smallest}')
