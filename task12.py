'''
Task 12
Seth Maurice-Brant
'''
valid = False

while not valid:
    validityChecker = 0
    letter = input("Enter letter: ")
    if len(letter) != 1:
        print("A single letter must be entered, not a string.")
    else:
        validityChecker += 1
   
    if not letter.isalpha():
        print("Please enter a letter, not whatever that was.")
    else:
        validityChecker += 1
    if validityChecker == 2:
        valid = True

print("ASCII char for input letter is: ", ord(letter))
