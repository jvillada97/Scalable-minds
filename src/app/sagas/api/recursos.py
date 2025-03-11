import json
from flask import Response
from flask import request
import seedwork.presentacion.api as api
from aplicacion.comandos import CrearSagas

bp = api.crear_blueprint('saga-proveedores', '/saga-proveedores')


@bp.route('/crear-proveedor', methods=['POST'])
def crear():
    try:     
        name = request.values.get('name')
        archivo_imagen = request.files.get('archivo_imagen')   
        resultado = CrearSagas(name, archivo_imagen).execute()
        return resultado    
    except Exception as e:
        print(e)


