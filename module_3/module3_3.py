gender = input("Enter your gender (male/female): ")
hem = int(input("Enter your hemoglobin g/l (just the number): "))

if gender == "male":
    if hem < 134:
        print("your hemoglobin is too low")
    elif 134 < hem < 195:
        print("your hemoglobin is normal")
    else:
        print("your hemoglobin is too high")
elif gender == "female":
    if hem < 117:
        print("your hemoglobin is too low")
    elif 117 < hem < 175:
        print("your hemoglobin is normal")
    else:
        print("your hemoglobin is too high")