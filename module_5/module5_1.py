import random

ammount = int(input("Enter number of dice: "))
summa = 0

for i in range(0,ammount):
    summa += random.randint(1,6)

print(summa)