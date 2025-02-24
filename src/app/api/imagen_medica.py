import app.seedwork.presentacion.api as api
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
        reserva_dict = request.json

        map_reserva = MapeadorImagenMedicaDTOJson()
        reserva_dto = map_reserva.externo_a_dto(reserva_dict)

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