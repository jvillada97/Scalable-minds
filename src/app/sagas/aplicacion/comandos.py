from flask import request, Blueprint
from flask import Response
from api.utils import crear_proveedor,  obtener_proveedor, crear_imagen_medica, eliminar_proveedor
import json
from aplicacion.mapeadores import MapeadorProveedorDTOJson
from infraestructura.repositorios import RepositorioSagaLogPostgresSQL
import uuid

class CrearSagas:
    def __init__(self, name, archivo_imagen):
        self.name = name
        self.archivo_imagen = archivo_imagen
        self.saga_log = RepositorioSagaLogPostgresSQL()
        
    def execute(self):        
        mapeador = MapeadorProveedorDTOJson()        
        proveedor = obtener_proveedor(self.name)        
        result_create = crear_proveedor(self.name)      
        self.saga_log.agregar('paso 1 - crear proveedor')
        print('paso 1 - crear proveedor')
        proveedor = obtener_proveedor(self.name)
        print(proveedor)
        imagen_medica = crear_imagen_medica(self.archivo_imagen)
        self.saga_log.agregar('paso 2 - crear imagen medica')     
        print('paso 2 - crear imagen medica')
        print(imagen_medica)
        if not imagen_medica:
            ##ELIMINAR LO CREADO
            self.saga_log.agregar('paso 3 - imagen fallida rollback proveedor')
            eliminar_proveedor(self.name)
            print('paso 3 - imagen fallida rollback proveedor')
            return Response(json.dumps({'msg':'No se pudo realizar la crecion del proveedor'}), status=409, mimetype='application/json')
        else:
            self.saga_log.agregar('paso 4 - proveedor creado')
            print('paso 4 - proveedor creado')
            self.saga_log.agregar('paso 5 - imagen medica creada')
            print('paso 5 - imagen medica creada')
            return Response(json.dumps({'msg':'Operacion Exitosa'}), status=200, mimetype='application/json')
        # except Exception as e:
        #     return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')




