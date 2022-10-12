# Task 6
# Seth Maurice-Brant

inValue = 0.5

while not isinstance(inValue, int):
    inValue = input("Enter number: ")
    try:
        inValue = int(inValue)
    except:
        pass

