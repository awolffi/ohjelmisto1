vuosi = int(input("Anna vuosiluku"))

if vuosi % 4 == 0:
    if vuosi % 100 == 0:
        if vuosi % 400 == 0:
            print("vuosi on karkausvuosi. ")
        else:
            print("vuosi ei ole karkausvuosi. ")
    else:
        print("vuosi on karkausvuosi. ")
else:
    print("vuosi ei ole karkausvuosi. ")
