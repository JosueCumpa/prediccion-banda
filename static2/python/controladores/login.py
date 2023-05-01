from static2.python.bd import obtener_conexion
import psycopg2


# def getAll():
#     try:
#         conexion = obtener_conexion()
#         semestres = []
#         with conexion.cursor() as cursor:
#             cursor.execute("select * from usuario()")
#             semestres = cursor.fetchall()
#         conexion.close()
#         return semestres
#     except psycopg2.Error as e:
#         raise e
        


def inicio_ses(nombre,clave):
    conexion = obtener_conexion()
    usuario=[]
    with conexion.cursor() as cursor:
        cursor.execute("SELECT nombre, clave FROM usuario WHERE nombre = %s  and clave = %s", (nombre,clave))
    usuario = cursor.fetchone()
    
    return usuario           