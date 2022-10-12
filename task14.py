'''
Task 14
Seth Maurice-Brant
'''

def DrawGrid(inNum):
    if not inNum in range(3,11):
        return "ERROR"
    sepUnit = "\n" + "+----"*inNum + "\n"
    divider = "|    " * inNum + "|"
    out = sepUnit + divider
    return out * inNum + sepUnit

# Test Grids

print(DrawGrid(7)) # GRID
print(DrawGrid(10)) # GRID
print(DrawGrid(2)) # ERROR
print(DrawGrid(11)) # ERROR
print(DrawGrid(3)) # GRID
