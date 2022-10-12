# Task 9
# Seth Maurice-Brant

isPositive = True
numbers = []

def CalcMean(numbers):
        divideBy = len(numbers)
        sumT = 0
        for entry in numbers:
            sumT += entry
        print("Mean: ",sumT / divideBy)
        quit()


while isPositive:
    newNum = input("Enter a number: ")
    if not newNum.isdigit():
        CalcMean(numbers)
        isPositive = False
    try:
        newNum = float(newNum)
    except:
        # Caught later on
        pass

    if newNum >= 0:
        numbers.append(newNum)
    else:
        isPositive = False
        CalcMean(numbers)

