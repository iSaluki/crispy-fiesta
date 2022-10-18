'''
Seth Maurice-Brant
Task 20
'''

def Seperate(inString):
    outString = ""
    for letter in inString:
        if letter.upper() == letter:
            outString += " "
        outString = outString + letter
    return outString

# Test Cases
print(Seperate("QuickBrownFox"))
print(Seperate("longRiver"))
print(Seperate("TheManWalksQuicklyAlongTheDarkRiver"))
print(Seperate("tImEtObReAkThIs"))
