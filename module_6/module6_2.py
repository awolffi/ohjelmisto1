import random

def dice(num):
    return random.randint(1, num)

num = int(input("Enter a number of dice faces: "))

while True:
    luck = dice(num)
    print(luck)
    if luck == num:
        break
