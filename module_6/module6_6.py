import math

def pizza_calculator(diameter, price):
    radius = float(diameter/2)
    area = (math.pi*radius*radius)/10000
    value = price/area
    return value

pizza1diameter = float(input("enter pizza 1 diameter (in cm): "))
pizza2diameter = float(input("enter pizza 2 diameter (in cm): "))
pizza1price = float(input("enter pizza 1 price (in euros): "))
pizza2price = float(input("enter pizza 2 price (in euros): "))

if pizza_calculator(pizza1diameter, pizza1price) > pizza_calculator(pizza2diameter, pizza2price):
    print("pizza 2 is better value for money")
elif pizza_calculator(pizza1diameter, pizza1price) == pizza_calculator(pizza2diameter, pizza2price):
    print("the value for money is the same in pizza 1 and pizza 2.")
else:
    print("pizza 1 is better value for money.")