# Task 11
# Seth Maurice-Brant

inNum = 0

while not inNum > 0 and inNum < 27:
    try:
        inNum = int(input("Enter a valid input between 1 and 26: "))
    except:
        print("Bad input - try again.")

inNum += 64
digit = chr(inNum)
character = ord(str(digit))

print(character, " ", digit)
