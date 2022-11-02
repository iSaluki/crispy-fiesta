'''
Task 34
Seth Maurice-Brant
'''

checkNum = input("Enter number to check beauty; ")

prevDigit = ""
for digit in checkNum:
    if int(digit) == int(prevDigit)+1:
        prevDigit = digit
    else:
        print("Not beatiful")
        break

