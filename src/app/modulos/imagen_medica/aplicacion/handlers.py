from app.modulos.imagen_medica.dominio.eventos import ImagenMedicaCreada
from app.seedwork.aplicacion.handlers import Handler
from app.modulos.imagen_medica.infraestructura.despachadores import Despachador

class HandlerReservaIntegracion(Handler):

    @staticmethod
    def handle_imagen_medica_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-reserva')

   


    