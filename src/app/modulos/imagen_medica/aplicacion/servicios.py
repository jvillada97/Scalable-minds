from app.seedwork.aplicacion.servicios import Servicio
from app.modulos.imagen_medica.dominio.entidades import ImagenMedica
from app.modulos.imagen_medica.dominio.fabricas import FabricaImagenMedica
from app.modulos.imagen_medica.infraestructura.fabricas import FabricaRepositorio
from app.modulos.imagen_medica.infraestructura.repositorios import RepositorioImagenMedicas
from .mapeadores import MapeadorReserva

from .dto import ImagenMedicaDTO

class ServicioReserva(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_vuelos(self):
        return self._fabrica_repositorio

    def crear_imagen_medica(self, reserva_dto: ImagenMedicaDTO) -> ImagenMedicaDTO:
        imagenMedica: ImagenMedica = self.fabrica_vuelos.crear_objeto(reserva_dto, MapeadorReserva())

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioImagenMedicas.__class__)
        repositorio.agregar(imagenMedica)

        return self.fabrica_vuelos.crear_objeto(imagenMedica, MapeadorReserva())

    def obtener_imagen_medica_por_id(self, id) -> ImagenMedicaDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioImagenMedicas.__class__)
        return repositorio.obtener_por_id(id).__dict__

