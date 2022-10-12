'''
Task 15
Seth Maurice-Brant
'''


# Incomplete - return to

def DrawGrid(row,col):
    if not row in range(3,11) and col in range(3,11):
        return "ERROR"
    sepUnit = "\n" + "+----"*row + "\n" # Row
    divider = "|    " * col + "|" # Column
    out = sepUnit + divider
    return out *row  + sepUnit

# Test Grids

print(DrawGrid(7,2)) # GRID
print(DrawGrid(10,10)) # GRID
print(DrawGrid(2,3)) # ERROR
print(DrawGrid(11,5)) # ERROR
print(DrawGrid(3,3)) # GRID
