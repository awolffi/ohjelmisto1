lev = float(input("Anna leviskat: "))
nau = float(input("Anna naulat: "))
luo = float(input("Anna luodit: "))

paino = luo*0.0133

paino = paino + (nau*32*0.0133)

paino = paino + (lev*20*32*0.0133)

gram = paino*1000

gramleft = int(paino) * 1000

final = gram - gramleft


print("massa nykymittojen mukaan: ")
print(f"{int(paino)} kilogrammaa ja {final:.2f}")
