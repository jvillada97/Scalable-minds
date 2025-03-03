from app.seedwork.aplicacion.comandos import Comando
from app.modulos.imagen_medica.aplicacion.dto import ImagenMedicaDTO
from app.modulos.imagen_medica.aplicacion.comandos.base import CrearImagenMedicaBaseHandler
from dataclasses import dataclass, field
from app.seedwork.aplicacion.comandos import ejecutar_commando as comando

from app.modulos.imagen_medica.dominio.entidades import ImagenMedica
from app.modulos.anonimizacion.dominio.entidades import Anonimizacion
from app.modulos.anonimizacion.aplicacion.mapeadores import MapeadorAnonimizacion
from app.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from app.modulos.imagen_medica.aplicacion.mapeadores import MapeadorImagenMedica
from app.modulos.imagen_medica.dominio.repositorios import RepositorioImagenMedicas, RepositorioEventosImagenMedicas
from app.modulos.anonimizacion.dominio.repositorios import RepositorioAnonimizacions, RepositorioEventosAnonimizacions

@dataclass
class CrearImagenMedica(Comando):
    url_image: str = field(default_factory=str)


class CrearImagenMedicaHandler(CrearImagenMedicaBaseHandler):
    
    def handle(self, comando: CrearImagenMedica):
        reserva_dto = ImagenMedicaDTO(
               url_imagen=comando.url_image)

        reserva: ImagenMedica = self.fabrica_imagen_medica.crear_objeto(reserva_dto, MapeadorImagenMedica())
        print(reserva)
        reserva.crear_propiedad(reserva)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioImagenMedicas)
        repositorio_eventos = self.fabrica_repositorio.crear_objeto(RepositorioEventosImagenMedicas)

        ##Recortar Imagen
        reserva: Anonimizacion = self.fabrica_imagen_medica.crear_objeto(reserva_dto, MapeadorAnonimizacion())        
        reserva.crear_propiedad(reserva)
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioAnonimizacions)
        repositorio_eventos = self.fabrica_repositorio.crear_objeto(RepositorioEventosAnonimizacions)
        
        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, reserva, repositorio_eventos_func=repositorio_eventos.agregar)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearImagenMedica)
def ejecutar_comando_crear_imagen_medica(comando: CrearImagenMedica):
    handler = CrearImagenMedicaHandler()
    handler.handle(comando)
    