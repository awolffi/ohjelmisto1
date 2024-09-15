import mysql.connector
from geopy.distance import geodesic


db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="K1rahV1!",
    database="flight_game",
    port=3306,
    autocommit=True,
    collation="utf8mb4_general_ci"
)

def get_airport_cord_by_areacode(code):
    sql = f'select latitude_deg, longitude_deg from airport where ident = "{code}"';
    cursor = db_connection.cursor()
    cursor.execute(sql)
    output = cursor.fetchall()
    return output

code1 = input("input 1. airport code: ")
code2 = input("input 2. airport code: ")
#(f"coord 1 is {get_airport_cord_by_areacode('EFHK')} and coord 2 is {get_airport_cord_by_areacode('KJFK')}")
coord1 = get_airport_cord_by_areacode(code1)
coord2 = get_airport_cord_by_areacode(code2)

distance = geodesic(coord1, coord2).kilometers
print(f"The distance between the airports is {distance:.2f} kilometers.")
