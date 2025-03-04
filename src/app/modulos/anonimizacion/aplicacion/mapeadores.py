from app.seedwork.aplicacion.dto import Mapeador as AppMap
from app.seedwork.dominio.repositorios import Mapeador as RepMap
from app.modulos.anonimizacion.dominio.entidades import Anonimizacion
from app.modulos.anonimizacion.dominio.objetos_valor import TipoArchivo, Archivo, Patologia, Modalidad, Etiqueta
from app.modulos.anonimizacion.aplicacion.dto import AnonimizacionDTO, DiagnosticoDTO, PatologiaDTO, ModalidadDTO, EtiquetaDTO, ArchivoDTO, TipoArchivoDTO
from werkzeug.datastructures import FileStorage
from dataclasses import field 
from datetime import datetime

class MapeadorAnonimizacionDTOJson(AppMap):   
    
    def externo_a_dto(self, externo: dict) -> AnonimizacionDTO:
        reserva_dto = AnonimizacionDTO()
        reserva_dto.id = externo.get('id')
        return reserva_dto  

    def dto_a_externo(self, dto: AnonimizacionDTO) -> dict:
        return dto.__dict__
    
class MapeadorAnonimizacion(RepMap):

    def obtener_tipo(self) -> type:        
        return Anonimizacion.__class__


    def entidad_a_dto(self, entidad: Anonimizacion) -> AnonimizacionDTO:
        compania_dto = AnonimizacionDTO()
        compania_dto.url_imagen = entidad.url_imagen
       
        return compania_dto
           

    def dto_a_entidad(self, dto: AnonimizacionDTO) -> Anonimizacion:
        imagenMedica = Anonimizacion()
        imagenMedica.url_imagen = dto.url_imagen     
        
        return imagenMedica




