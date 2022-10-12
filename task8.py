# Task 8
# Seth Maurice-Brant

import random

def rollDice(dCount, sCount):
    results = []
    while dCount > 0:
        roll = random.randint(1,sCount)
        results.append(roll)
        dCount -= 1
    return results

print(rollDice(7,12))


