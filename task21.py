'''
Task 21
Seth Maurice-Brant
'''


inWord = input("Enter sentence: ").lower()

wasSpace = True

outWord = ""

for digit in inWord:
    if digit == " ":
        wasSpace = True
        continue
    if wasSpace:
        digit = digit.upper()
        wasSpace = False
    outWord = outWord + digit
print(outWord)
