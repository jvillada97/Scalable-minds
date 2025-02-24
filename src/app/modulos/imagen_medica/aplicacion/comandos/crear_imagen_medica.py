from app.seedwork.aplicacion.comandos import Comando
from app.modulos.imagen_medica.aplicacion.dto import ImagenMedicaDTO
from app.modulos.imagen_medica.aplicacion.comandos.base import CrearImagenMedicaBaseHandler
from dataclasses import dataclass, field
from app.seedwork.aplicacion.comandos import ejecutar_commando as comando

from app.modulos.imagen_medica.dominio.entidades import ImagenMedica
from app.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from app.modulos.imagen_medica.aplicacion.mapeadores import MapeadorImagenMedica
from app.modulos.imagen_medica.infraestructura.repositorios import RepositorioImagenMedicas
@dataclass
class CrearImagenMedica(Comando):
    url_image: str = field(default_factory=str)


class CrearReservaHandler(CrearImagenMedicaBaseHandler):
    
    def handle(self, comando: CrearImagenMedica):
        reserva_dto = ImagenMedicaDTO(
               url_imagen=comando.url_image)

        reserva: ImagenMedica = self.fabrica_imagen_medica.crear_objeto(reserva_dto, MapeadorImagenMedica())
        print(reserva)
        reserva.crear_propiedad(reserva)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioImagenMedicas.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, reserva)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearImagenMedica)
def ejecutar_comando_crear_imagen_medica(comando: CrearImagenMedica):
    handler = CrearReservaHandler()
    handler.handle(comando)
    