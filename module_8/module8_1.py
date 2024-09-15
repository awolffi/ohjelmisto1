import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="K1rahV1!",
    database="flight_game",
    port=3306,
    autocommit=True,
    collation="utf8mb4_general_ci"
)

def get_airport_by_icao(icao):
    sql = f'SELECT name, municipality FROM airport WHERE ident = "{icao}"'
    cursor = db_connection.cursor()
    cursor.execute(sql)
    airport_data = cursor.fetchall()
    return airport_data

icao = input("enter icao number: ")
print(f"The airport name and location for the given icao number is {get_airport_by_icao(icao)}")
