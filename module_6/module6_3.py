def convert(gallons):
    liters = gallons*3.785
    return liters

u_input = float(input("fuel in gallons: "))

while u_input > 0:
    print(convert(u_input))
    u_input = float(input("fuel in gallons: "))
