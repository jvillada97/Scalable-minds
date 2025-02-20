import app.seedwork.presentacion.api as api
import app.seedwork.presentacion.api as api
import json
from app.modulos.recursos.aplicacion.servicios import ServicioReserva
from app.modulos.recursos.aplicacion.dto import RecursoDTO
from app.seedwork.dominio.excepciones import ExcepcionDominio

from flask import redirect, render_template, request, session, url_for
from flask import Response
from app.modulos.recursos.aplicacion.mapeadores import MapeadorReservaDTOJson
bp = api.crear_blueprint('recurso', '/recurso')


@bp.route('/recurso', methods=('POST',))
def recurso():
    try:
        reserva_dict = request.json

        map_reserva = MapeadorReservaDTOJson()
        reserva_dto = map_reserva.externo_a_dto(reserva_dict)

        sr = ServicioReserva()
        dto_final = sr.crear_recurso(reserva_dto)

        return map_reserva.dto_a_externo(dto_final)
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/recurso', methods=('GET',))
@bp.route('/recurso/<id>', methods=('GET',))
def dar_recurso(id=None):
    if id:
        sr = ServicioReserva()
        
        return sr.obtener_recurso_por_id(id)
    else:
        return [{'message': 'GET!'}]