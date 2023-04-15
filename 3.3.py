#3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. 
# If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85. 

# Prompt the user to enter a score between 0.0 and 1.0
score = input("Enter a score between 0.0 and 1.0: ")

try:
    # Convert the score input to a float
    score = float(score)
    
    # Check if the score is out of range (greater than 1.0)
    if score > 1.0:
        print("Value out of range")
        quit()
    
    # Check if the score is an A
    elif score >= 0.9:
        print("A")
    
    # Check if the score is a B
    elif score >= 0.8:
        print("B")
    
    # Check if the score is a C
    elif score >= 0.7:
        print("C")
    
    # Check if the score is an F
    elif score < 0.6:
        print("F")
    
    # Check if the score is out of range (less than 0)
    elif score < 0:
        print("Value out of range")
        quit()

# If there's an error, print an error message
except:
    print("Entered value was incorrect.")
