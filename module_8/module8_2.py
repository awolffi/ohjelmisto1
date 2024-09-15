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


def get_airport_type_by_areacode(code):
    sql = f'select type, count(*) as count from airport where iso_country = "{code}" group by type'
    #sql = 'select type from airport limit 10'
    cursor = db_connection.cursor()
    cursor.execute(sql)
    output = cursor.fetchall()
    return output

user_input = input("Enter your airport area code: ")

result = get_airport_type_by_areacode(user_input)

for type, count in result:
    print(f"in {user_input} there are {count} {type},")


