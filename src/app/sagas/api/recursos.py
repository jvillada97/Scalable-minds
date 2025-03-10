import json
from flask import Response
from flask import request
import seedwork.presentacion.api as api
from aplicacion.comandos import CrearSagas

bp = api.crear_blueprint('saga-proveedores', '/saga-proveedores')


@bp.route('/crear-proveedor', methods=['POST'])
def crear():
    try:
        proveedor_dict = request.get_json()
        resultado = CrearSagas(proveedor_dict).execute()
        return resultado 
    except Exception as e:
        print(e)


