from pydispatch import dispatcher
from app.modulos.proveedor.aplicacion.handlers import HandlerReservaIntegracion

dispatcher.connect(HandlerReservaIntegracion.handle_proveedor_creada, signal='ProveedorCreadaDominio')
