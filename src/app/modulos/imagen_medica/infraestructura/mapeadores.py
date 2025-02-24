""" Mapeadores para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from app.seedwork.dominio.repositorios import Mapeador
from app.modulos.imagen_medica.dominio.objetos_valor import Archivo, TipoArchivo, Etiqueta,Patologia,Modalidad
from app.modulos.imagen_medica.dominio.entidades import ImagenMedica, Diagnostico
from app.modulos.imagen_medica.infraestructura.dto import ImagenMedica as ImagenMedicaDTO

class MapeadorReserva(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'   

    def obtener_tipo(self) -> type:
        return ImagenMedica.__class__

    def entidad_a_dto(self, entidad: ImagenMedica) -> ImagenMedicaDTO:
        
        reserva_dto = ImagenMedicaDTO()
        reserva_dto.url_imagen = entidad.url_imagen
        return reserva_dto

    def dto_a_entidad(self, dto: ImagenMedicaDTO) -> ImagenMedica:
        reserva = ImagenMedica(dto.url_imagen)   
        
        return reserva