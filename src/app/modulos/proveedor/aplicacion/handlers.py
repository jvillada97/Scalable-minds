from app.modulos.proveedor.dominio.eventos import ProveedorCreada
from app.seedwork.aplicacion.handlers import Handler
from app.modulos.proveedor.infraestructura.despachadores import Despachador

class HandlerReservaIntegracion(Handler):

    @staticmethod
    def handle_proveedor_eliminada(evento):
        try:
            despachador = Despachador()
            despachador.publicar_evento_eliminada(evento, 'eventos-proveedor-eliminada')
        except Exception as e:
            print(f"ERROR AL PUBLICAR {e}")

    @staticmethod
    def handle_proveedor_creada(evento):
        try:
            despachador = Despachador()
            despachador.publicar_evento(evento, 'eventos-proveedor')
        except Exception as e:
            print(f"ERROR AL PUBLICAR {e}")

   


    