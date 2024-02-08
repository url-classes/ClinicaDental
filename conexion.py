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

cursor = connection.cursor()

# Consulta SQL para seleccionar datos
sql = "SELECT * FROM material"
cursor.execute(sql)

# Obtiene todos los resultados
resultados = cursor.fetchall()

if len(resultados) > 0:
    # Muestra los resultados en formato de tabla
    print("ID\t\t\tNombre\t\t\tSerie o Modelo\t\t\tCantidad\t\t\tPrecio Individual\t\t\tPrecio Total")
    for row in resultados:
        print(f"{str(row[0]).ljust(15)}{str(row[1]).ljust(20)}{str(row[2]).ljust(25)}{str(row[3]).ljust(15)}{str(row[4]).ljust(20)}{str(row[5])}")
else:
    print("0 resultados")

"""# Cierra el cursor y la conexión
cursor.close()
connection.close()"""

"""finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("La conexión a MySQL está cerrada")"""








