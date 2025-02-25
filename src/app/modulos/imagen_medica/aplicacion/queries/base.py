from app.seedwork.aplicacion.queries import QueryHandler
from app.modulos.imagen_medica.infraestructura.fabricas import FabricaVista
from app.modulos.imagen_medica.dominio.fabricas import FabricaImagenMedica

class ImagenMedicaQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_vista: FabricaVista = FabricaVista()
        self._fabrica_imagen_medica: FabricaImagenMedica = FabricaImagenMedica()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_vista
    
    @property
    def fabrica_imagen_medica(self):
        return self._fabrica_imagen_medica    