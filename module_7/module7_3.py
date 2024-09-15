airports={}
while True:

    user_command = input("do you want to enter a new airport, fetch the information of an existing airport or quit? type:(enter, fetch or quit): ")

    if user_command == "enter":
        icao_number = input("enter the icao number: ")
        airport_name = input("enter the airport name: ")
        airports[icao_number] = airport_name
    elif user_command == "fetch":
        icao = input("enter the icao number: ")
        if icao in airports:
            print(f"The airport name for {icao} icao number is {airports[icao]}")
        else:
            print("invalid icao number")
    elif user_command == "quit":
        print("program is qitting...")
        break
    else:
        print("invalid input")