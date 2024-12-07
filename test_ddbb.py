import pyodbc

def test_sql_server_connection():
    try:
        # Definir la cadena de conexión
        conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=127.0.0.1,1433;DATABASE=cavipetrol;UID=sa;PWD=C4vip3tr0l'
        
        # Intentar conectar
        conn = pyodbc.connect(conn_str)
        
        # Realizar una consulta simple
        cursor = conn.cursor()
        cursor.execute("SELECT @@version;")  # Consulta para obtener la versión de SQL Server
        row = cursor.fetchone()
        
        # Mostrar el resultado
        if row:
            print("Conexión exitosa a SQL Server!")
            print("Versión de SQL Server:", row[0])
        
        # Cerrar la conexión
        cursor.close()
        conn.close()

    except Exception as e:
        print("Error al conectar a SQL Server:", e)

# Llamar a la función para probar la conexión
test_sql_server_connection()
