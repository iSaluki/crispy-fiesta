'''
Task 37
Seth Maurice-Brant
'''

initialPrimes = []

iNum = "a"

while not iNum.isdigit():
    iNum = input("Enter number: ")
iNum = int(iNum)

isPrime = True
if iNum%2==0:
    print("Not prime - even")
else:
    for num in range(3,iNum**0.5):
        if iNum % num == 0:
            isPrime = False
            print("Not prime, appears as multiple of", num)
if isPrime:
    print("It is prime")
