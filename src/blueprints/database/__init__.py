from flask import Blueprint

maestros_bp = Blueprint(
    'maestros',
    __name__,
    url_prefix='/api/maestros' # <--- Debe ir DENTRO de los paréntesis, separado por comas
)