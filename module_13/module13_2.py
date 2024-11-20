from flask import Flask
import mysql.connector


db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="flight_game",
    port=3306,
    autocommit=True,
    collation="utf8mb4_general_ci"
)

app = Flask(__name__)
@app.route('/airport/<icao>')
def get_name_by_icao(icao):
    sql = f'SELECT name FROM airport WHERE ident = "{icao}"'
    cursor = db_connection.cursor()
    cursor.execute(sql)
    airport_name = cursor.fetchall()
    
    sql = f'SELECT municipality FROM airport WHERE ident = "{icao}"'
    cursor = db_connection.cursor()
    cursor.execute(sql)
    airport_municipality = cursor.fetchall()
    
    response = {
        "ICAO" : icao,
        "Name" : airport_name,
        "Location" : airport_municipality
    }

    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
    





