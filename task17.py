'''
Task 17
Seth Maurice-Brant
'''

def PalindromeChecker(testword):
    if len(testword) < 4:
        return False


    if testword == testword[::-1]:
        return True
    else:
        return False


# Tests

print(PalindromeChecker("fox")) # FALSE
print(PalindromeChecker("foof")) # TRUE
print(PalindromeChecker("figure")) # FALSE
print(PalindromeChecker("sethhtes")) # TRUE
