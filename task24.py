'''
Task 24
Seth Maurice-Brant
'''

def AnagramCheck(testSent1,testSent2):
    ts1 = []
    ts2 = []
    for letter in testSent1:
        ts1.append(letter)
    for letter in testSent2:
        ts2.append(letter)
    ts1.sort()
    ts2.sort()
    if ts1 == ts2:
        return True
    else:
        return False


# Test Cases
print(AnagramCheck("bob","bob")," expected = True") # True
print(AnagramCheck("ship","pish")," expected = True") # True
print(AnagramCheck("man","nan"), " expected = False") # False
print(AnagramCheck("Sweden","Swindon"), " expected = False") # False - They are not the same father
print(AnagramCheck("nloi", "lion"), " expected = True") # True
