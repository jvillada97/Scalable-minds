from app.seedwork.aplicacion.comandos import Comando
from app.modulos.imagen_medica.aplicacion.dto import ImagenMedicaDTO
from app.modulos.anonimizacion.aplicacion.dto import AnonimizacionDTO
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
        anonimizacion_dto = AnonimizacionDTO(
               url_imagen=comando.url_image)

        anonimizacion: Anonimizacion = self.fabrica_anonimizacion.crear_objeto(anonimizacion_dto, MapeadorAnonimizacion())        
        anonimizacion.crear_propiedad(reserva)
        repositorio_anonimizacion = self.fabrica_repositorio_anonimizacion.crear_objeto(RepositorioAnonimizacions)
        repositorio_eventos_anonimizacion = self.fabrica_repositorio_anonimizacion.crear_objeto(RepositorioEventosAnonimizacions)
       
        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, reserva)
        UnidadTrabajoPuerto.registrar_batch(repositorio_eventos.agregar, reserva)    
        UnidadTrabajoPuerto.registrar_batch(repositorio_anonimizacion.agregar, reserva)
        UnidadTrabajoPuerto.registrar_batch(repositorio_eventos_anonimizacion.agregar, reserva)    
        
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearImagenMedica)
def ejecutar_comando_crear_imagen_medica(comando: CrearImagenMedica):
    handler = CrearImagenMedicaHandler()
    handler.handle(comando)
    