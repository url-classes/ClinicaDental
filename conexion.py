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
    print("ID\tNombre\tSerie o Modelo\tCantidad\tPrecio Individual\tPrecio Total")
    for row in resultados:
        print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}")
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








