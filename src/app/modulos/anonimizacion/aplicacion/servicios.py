from app.seedwork.aplicacion.servicios import Servicio
from app.modulos.anonimizacion.dominio.entidades import Anonimizacion
from app.modulos.anonimizacion.dominio.fabricas import FabricaAnonimizacion
from app.modulos.anonimizacion.infraestructura.fabricas import FabricaRepositorio
from app.modulos.anonimizacion.infraestructura.repositorios import RepositorioAnonimizacions
from app.modulos.anonimizacion.aplicacion.mapeadores import MapeadorAnonimizacion


from .dto import AnonimizacionDTO

class ServicioAnonimizacion(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_vuelos(self):
        return self._fabrica_repositorio

    def crear_anonimizacion(self, reserva_dto: AnonimizacionDTO) -> AnonimizacionDTO:
        # Guardar la imagen en una carpeta
       

        # Crear la entidad Anonimizacion
        Anonimizacion: Anonimizacion = self.fabrica_vuelos.crear_objeto(reserva_dto, MapeadorAnonimizacion())       

        # Guardar la entidad en el repositorio
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioAnonimizacions.__class__)
        repositorio.agregar(Anonimizacion)

        return self.fabrica_vuelos.crear_objeto(Anonimizacion, MapeadorAnonimizacion())

    def obtener_anonimizacion_por_id(self, id) -> AnonimizacionDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioAnonimizacions.__class__)
        anonimizacion = repositorio.obtener_por_id(id)
        
        # Leer el archivo de imagen desde la URL
        with open(anonimizacion.url_imagen, 'rb') as file:
            imagen_data = file.read()
        
        # Crear el DTO y agregar la imagen
        anonimizacion_dto = self.fabrica_vuelos.crear_objeto(anonimizacion, MapeadorAnonimizacion())      
        
        return anonimizacion_dto

