import app.seedwork.presentacion.api as api
import uuid
import app.seedwork.presentacion.api as api
import json
from app.modulos.proveedor.aplicacion.servicios import ServicioProveedor
from app.modulos.proveedor.aplicacion.dto import ProveedorDTO
from app.seedwork.dominio.excepciones import ExcepcionDominio
from werkzeug.utils import secure_filename
from flask import redirect, render_template, request, session, url_for
from flask import Response, send_file
from app.modulos.proveedor.aplicacion.mapeadores import MapeadorProveedorDTOJson
from app.modulos.proveedor.aplicacion.comandos.crear_provedor import CrearProveedor
from app.modulos.proveedor.aplicacion.queries.obtener_proveedor import ObtenerProveedorPorNombre

import os
import io
import mimetypes
import zipfile
from app.seedwork.aplicacion.queries import ejecutar_query
from app.seedwork.aplicacion.comandos import ejecutar_commando

bp = api.crear_blueprint('proveedor', '/proveedor')


@bp.route('/', methods=('POST',))
def proveedor():
    try:        
       
        reserva_dict = request.json

        map_reserva = MapeadorProveedorDTOJson()
        reserva_dto = map_reserva.externo_a_dto(reserva_dict)
      
        comando = CrearProveedor(
            name=reserva_dto.name,
        )
        ejecutar_commando(comando)
        return {"message": "Proveedor creado exitosamente"}, 201
    
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    
@bp.route('/<name>', methods=['GET'])
def dar_proveedor_por_nombre_usando_query(name):
    try:
         map_compania = MapeadorProveedorDTOJson()
         print(name)
         query_resultado = ejecutar_query(ObtenerProveedorPorNombre(name))
         
         if query_resultado.resultado is None:             
            return Response(json.dumps(dict(error="No se encontro Proveedor")), status=400, mimetype="application/json")
        
         compania = map_compania.dto_a_externo(query_resultado.resultado)
         return compania
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=404, mimetype='application/json')