def purge_exe(lista):
    for i in lista:
        if i % 2 != 0:
            lista.remove(i)

    return lista

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)
print(purge_exe(lista))
