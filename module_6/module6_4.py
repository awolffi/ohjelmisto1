def summa(lista):
    numbers = 0
    for i in lista:
        numbers = numbers + i
    return numbers

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(summa(test_list))