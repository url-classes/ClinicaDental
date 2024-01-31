import mysql.connector
from mysql.connector import Error

try:

    connection = mysql.connector.connect(
        host='localhost',       
        user='root',           
        password='root',   
        database='clinica_dental'    
    )

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Conectado a MySQL Server versión", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Conectado a la base de datos: ", record)

except Error as e:
    print("Error al conectar a MySQL", e)

"""finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("La conexión a MySQL está cerrada")"""








