import random

tries = int(input("Anna kokonaisluku: "))
total = tries
n = 0
while tries > 0:
    hor = random.uniform(-1, 1)
    ver = random.uniform(-1, 1)
    if hor**2+ver**2 < 1:
        n = n+1
    tries = tries - 1

vast = (4*n)/total

print(vast)




