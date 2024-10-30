import requests

api = "fa9b667384a9799661ebea6fe00cf7f4"

city = input("enter city name: ")
try:
    request = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"
    response = requests.get(request).json()
    print(f"in city {city} the weather status is: {response["weather"][0]["description"]} and the temperature is: {(response["main"]["temp"]) - 273.15:.2f} degrees celcius")

except:
    print("didnt work")
