from app.seedwork.aplicacion.dto import Mapeador as AppMap
from app.seedwork.dominio.repositorios import Mapeador as RepMap
from app.modulos.imagen_medica.dominio.entidades import ImagenMedica, Diagnostico
from app.modulos.imagen_medica.dominio.objetos_valor import TipoArchivo, Archivo, Patologia, Modalidad, Etiqueta
from app.modulos.imagen_medica.aplicacion.dto import ImagenMedicaDTO, DiagnosticoDTO, PatologiaDTO, ModalidadDTO, EtiquetaDTO, ArchivoDTO, TipoArchivoDTO
from werkzeug.datastructures import FileStorage
from dataclasses import field 
from datetime import datetime

class MapeadorImagenMedicaDTOJson(AppMap):   
    
    def externo_a_dto(self, externo: dict) -> ImagenMedicaDTO:
        reserva_dto = ImagenMedicaDTO()
        reserva_dto.id = externo.get('id')
        return reserva_dto  

    def dto_a_externo(self, dto: ImagenMedicaDTO) -> dict:
        return dto.__dict__
    
class MapeadorImagenMedica(RepMap):

    def obtener_tipo(self) -> type:        
        return ImagenMedica.__class__


    def entidad_a_dto(self, entidad: ImagenMedica) -> ImagenMedicaDTO:
        compania_dto = ImagenMedicaDTO()
        compania_dto.url_imagen = entidad.url_imagen  
        
        return compania_dto
           

    def dto_a_entidad(self, dto: ImagenMedicaDTO) -> ImagenMedica:
        imagenMedica = ImagenMedica()
        imagenMedica.url_imagen = dto.url_imagen     
        
        return imagenMedica



