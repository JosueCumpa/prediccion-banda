import psycopg2
from psycopg2 import DatabaseError
# def obtener_conexion():
#     return psycopg2.connect(host='127.0.0.1',
#                             port=5432,
#                             database='bd_prediccion',
#                             user='postgres',
#                             password='12'
#                             )
#Pruba de conexion directa
# try:
#     connection=psycopg2.connect(
#         host='localhost',
#         user='postgres',
#         password='12',
#         database='bd_prediccion'
#     )
#     print("Conexion exitosa")
#     cursor=connection.cursor()
#     cursor.execute("Select * from usuario")
#     row=cursor.fetchall()
#     for rows in row:
#         print(row)
# except Exception as ex:
#     print(ex)

#Conexion pc original
""" def obtener_conexion():
    try:
        return psycopg2.connect(
            host='localhost',
            user='postgres',
            password='12',
            database='bd_prediccion'
        )
    except DatabaseError as ex:
        raise ex """
# Conexion servidor
def obtener_conexion():
    try:
        return psycopg2.connect(
            host='localhost',
            user='postgres',
            password='2314',
            database='bd_prediccion'
        )
    except DatabaseError as ex:
        raise ex