luku = int(input("anna kokonaisluku luku: "))

if luku > 1:
    for x in range(2, (luku//2)+1):
        if luku % x == 0:
            print(f"luku {luku} ei ole alkuluku.")
            break
    else:
        print(f"luku {luku} on alkuluku.")
else:
    print(f"luku {luku} ei ole alkuluku.")