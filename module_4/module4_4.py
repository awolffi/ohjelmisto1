import random

num = random.randint(1, 10)
print(num)
guess = int(input("Arvaa luku (1 - 10): "))

if guess:
    while num != guess:
        if guess < num:
            print("Liian pieni arvaus ")
        elif guess > num:
            print("Liian suuri arvaus ")

        guess = int(input("Arvaa luku (1 - 10): "))
    print("Oikein")