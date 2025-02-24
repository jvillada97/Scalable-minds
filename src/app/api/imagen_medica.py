import app.seedwork.presentacion.api as api
import json
from app.modulos.imagen_medica.aplicacion.servicios import ServicioReserva
from app.modulos.imagen_medica.aplicacion.dto import ImagenMedicaDTO
from app.seedwork.dominio.excepciones import ExcepcionDominio

from flask import redirect, render_template, request, session, url_for
from flask import Response
from app.modulos.imagen_medica.aplicacion.mapeadores import MapeadorImagenMedicaDTOJson
bp = api.crear_blueprint('imagen-medica', '/imagen-medica')


@bp.route('/imagen-medica', methods=('POST',))
def imagenMedica():
    try:
        print("Paso 1")
        reserva_dict = request.json
        id = reserva_dict.get('id')
        url_imagen = reserva_dict.get('url_imagen')
        archivo_imagen = request.files.get('archivo_imagen')
        print(f"ID: {id}")
        print(f"URL Imagen: {url_imagen}")
        print(f"Archivo Imagen: {archivo_imagen.filename}")
        map_reserva = MapeadorImagenMedicaDTOJson()
        reserva_dto = map_reserva.externo_a_dto({
            'id': id,
            'url_imagen': url_imagen,
            'archivo_imagen': archivo_imagen
        })

        sr = ServicioReserva()
        dto_final = sr.crear_imagen_medica(reserva_dto)

        return map_reserva.dto_a_externo(dto_final)
    
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/imagen-medica', methods=('GET',))
@bp.route('/imagen-medica/<id>', methods=('GET',))
def dar_recurso(id=None):
    if id:
        sr = ServicioReserva()
        
        return sr.obtener_imagen_medica_por_id(id)
    else:
        return [{'message': 'GET!'}]
    
@bp.route("/ping")
def health():
    return {"status": "pong"}