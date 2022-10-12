'''
Task 14
Seth Maurice-Brant
'''

def DrawGrid(inNum):
    if not inNum in range(3,11):
        return "ERROR"
    print("-  -  -  -")
    print("|\n\t|\n|\n\t|\n|\n\t|\n|\n\t|")
    print("-  -  -  -")

DrawGrid(7)
