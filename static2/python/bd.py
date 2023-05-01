import psycopg2

def obtener_conexion():
    return psycopg2.connect(host='localhost',
                            database='bd_prediccion',
                            user='postgres',
                            password='12'
                            )