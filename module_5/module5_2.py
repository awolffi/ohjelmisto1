my_list = []

luku = input("anna luku: ")
while luku != "":
    luku = float(luku)
    my_list.append(luku)
    luku = input("anna luku: ")

reversed_list = sorted(my_list, reverse=True)
reversed_list = [int(num) for num in reversed_list]

print(reversed_list[:4])
