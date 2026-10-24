from flask import Blueprint, jsonify, request
from blueprints.database import mysql

alumnos_bp = Blueprint(
    'alumnos',
    __name__,
    url_prefix='/api/alumnos'
)

def fila_a_diccionario(cursor, fila):
    # Corregido: Definimos 'columnas' en plural para que coincida en el zip
    columnas = [columna[0] for columna in cursor.description]
    return dict(zip(columnas, fila))

@alumnos_bp.route("/alumnos", methods=['GET'])
def listar_alumnos():
    cursor = None

    try:
        cursor = mysql.connection.cursor()
        cursor.execute(
            """
            SELECT * FROM alumnos
            """)
        datos = cursor.fetchall()
        alumnos = [
            fila_a_diccionario(cursor, fila)
            for fila in datos
        ]
        # Corregido: Se usan llaves {} y se añade la coma faltante
        return jsonify({
            'alumnos': alumnos,
            'mensajes': 'lista de alumnos',
            'exito': True
        }), 200

    except Exception as e:
        print(e)  # Opcional: te ayuda a ver el error exacto en consola si falla la BD
        return jsonify({
            'mensaje': 'Error al consultar alumnos',
            'exito': False
        }), 500

    finally:
        if cursor is not None:
            cursor.close()