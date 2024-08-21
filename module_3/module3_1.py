pituus = float(input("syota kuhan pituus (cm): "))

if pituus < 37:
    print("Kuha on alamittainen. Heita takaisin veteen! ")
    print(f"{37-pituus} cm liian pieni oli")
else:
    print("ei tarvi laskea veteen, saat syoda!")