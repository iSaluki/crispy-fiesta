'''
Task 31
Seth Maurice-Brant
'''
def FormatPNumber(unformatted):
    unformatted.insert(5, " ")
    formatted = ""
    for digit in unformatted:
        formatted += str(digit)
    print(formatted)

# Only attempting standard phone number formats

FormatPNumber([0,1,3,8,6,7,6,5,5,8,8])
FormatPNumber([0,7,4,9,8,9,6,2,3,1,9])
FormatPNumber([1,1,1,1,1,1,1,1,1,1,1])
