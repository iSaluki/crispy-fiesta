def ValidateString(inStr):
    validity = 0

    if len(inStr) == 2:
        validity += 1
    else:
        validity = -100
    
    if inStr[0].upper() == "A" or "B" or "C":
        validity += 1
    else:
        validity = -100

    try:
        if int(inStr[1]) in range(1,4):
            validity += 1
        else:
             validity = -100
    except:
        validty = -100
    out1 = 0
    out2 = 0
    if validity == 3:
       # Would rather use a switch statement here
        if  inStr[0].upper() == "A":
            out1 = 1
        if inStr[0].upper() == "B":
             out1 = 2
        if  inStr[0].upper() == "C":
            out1 = 3
        out2 = int(inStr[1])
        
        return (out1, out2)
    else:
        return (False)

# Test Cases

print(ValidateString("A2")) # 1,2
print(ValidateString("BEELZEBUB")) # False
print(ValidateString("C3")) # 3,3
print(ValidateString("C4")) # False
print(ValidateString("A0")) # False
