# Task 10
# Seth Maurice-Brant

validInputs = []
stopped = False

while not stopped:
    posInt = input("Enter positive integer: ")

    if posInt.isdigit():
        posInt = int(posInt)
        validInputs.append(posInt)
    else:
        print("Bad input, stopping")
        validInputs.sort()
        print("Smallest=",validInputs[0])
        print("Largest=",validInputs[-1])
        stopped = True

