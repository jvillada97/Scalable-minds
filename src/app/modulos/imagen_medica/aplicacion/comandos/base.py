from app.seedwork.aplicacion.comandos import ComandoHandler
from app.modulos.imagen_medica.infraestructura.fabricas import FabricaRepositorio
from app.modulos.anonimizacion.infraestructura.fabricas import FabricaRepositorio as FabricaRepositorioAnonimizacion
from app.modulos.imagen_medica.dominio.fabricas import FabricaImagenMedica
from app.modulos.anonimizacion.dominio.fabricas import FabricaAnonimizacion
class CrearImagenMedicaBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_repositorio_anonimizacion: FabricaRepositorioAnonimizacion = FabricaRepositorioAnonimizacion()
        self._fabrica_imagen_medica: FabricaImagenMedica = FabricaImagenMedica()
        self._fabrica_anonimizacion: FabricaAnonimizacion = FabricaAnonimizacion()
        
    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_imagen_medica(self):
        return self._fabrica_imagen_medica    
    
    @property
    def fabrica_repositorio_anonimizacion(self):
        return self._fabrica_repositorio_anonimizacion    
    
    @property
    def fabrica_anonimizacion(self):
        return self._fabrica_anonimizacion  