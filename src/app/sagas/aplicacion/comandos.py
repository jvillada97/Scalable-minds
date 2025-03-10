from flask import request, Blueprint
from flask import Response
from api.utils import crear_proveedor,  obtener_proveedor
import json
from aplicacion.mapeadores import MapeadorProveedorDTOJson
from infraestructura.repositorios import RepositorioSagaLogPostgresSQL
import uuid

class CrearSagas:
    def __init__(self, post_request):
        self.post_request = post_request
        self.saga_log = RepositorioSagaLogPostgresSQL()
        
    def execute(self):        
        mapeador = MapeadorProveedorDTOJson()
        saga_proveedor = mapeador.externo_a_dto(self.post_request)  
        proveedor = obtener_proveedor(saga_proveedor.name)
        print(proveedor)
        result_create = crear_proveedor(saga_proveedor)
        print(result_create)
        self.saga_log.agregar('paso 1 - crear proveedor')
        proveedor = obtener_proveedor(saga_proveedor.name)
        if not proveedor:
            ##ELIMINAR LO CREADO
            self.saga_log.agregar('paso 2 - eliminar proveedor fallido')
            return Response(json.dumps({'msg':'No se pudo realizar la crecion del proveedor'}), status=409, mimetype='application/json')
        else:
            self.saga_log.agregar('paso 3 - proveedor creado')
            return proveedor
        # except Exception as e:
        #     return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')




