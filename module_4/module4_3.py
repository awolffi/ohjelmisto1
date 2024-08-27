num = input("Enter a number: ")

if not num:
    print("no number. ")
else:
    float(num)
numin = num
numax = num


while num:
    if float(num)<float(numin):
        numin = num
    elif float(num)>float(numax):
        numax = num
    num = input("Enter a number: ")

    if not num:
        print(f"{numin} on pienin ja {numax} on suurin")


