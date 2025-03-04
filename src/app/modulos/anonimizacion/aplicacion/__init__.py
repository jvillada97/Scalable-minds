from pydispatch import dispatcher
from app.modulos.anonimizacion.aplicacion.handlers import HandlerReservaIntegracion

dispatcher.connect(HandlerReservaIntegracion.handle_anonimizacion_creada, signal='AnonimizacionCreadaDominio')
