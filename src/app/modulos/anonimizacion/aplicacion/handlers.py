from app.modulos.anonimizacion.dominio.eventos import AnonimizacionCreada
from app.seedwork.aplicacion.handlers import Handler
from app.modulos.anonimizacion.infraestructura.despachadores import Despachador

class HandlerReservaIntegracion(Handler):

    @staticmethod
    def handle_anonimizacion_creada(evento):
        try:
            despachador = Despachador()
            despachador.publicar_evento(evento, 'eventos-anonimizacion')
        except Exception as e:
            print(f"ERROR AL PUBLICAR {e}")

   


    