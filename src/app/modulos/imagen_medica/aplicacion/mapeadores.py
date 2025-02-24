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
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'  

    def obtener_tipo(self) -> type:        
        return ImagenMedica.__class__


    def entidad_a_dto(self, entidad: ImagenMedica) -> ImagenMedicaDTO:
        compania_dto = ImagenMedicaDTO()
        compania_dto.url_imagen = entidad.url_imagen
        # fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        # fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)       
        # tipoArchivo = TipoArchivoDTO(entidad.tipoArchivo.nombres, entidad.tipoArchivo.extension)
        # archivo = ArchivoDTO(entidad.archivo.identificador, entidad.archivo.ruta)
        # patologia = PatologiaDTO(entidad.diagnostico.patologia.nombre)
        # modalidad = ModalidadDTO(entidad.diagnostico.modalidad.nombre)
        # etiqueta = EtiquetaDTO(entidad.diagnostico.etiqueta.identificador)
        # diagnostico = DiagnosticoDTO(entidad.diagnostico.fecha_creacion, entidad.diagnostico.fecha_actualizacion,
        #                              entidad.diagnostico.id, etiqueta, modalidad, patologia)
        
        return compania_dto
           

    def dto_a_entidad(self, dto: ImagenMedicaDTO) -> ImagenMedica:
        imagenMedica = ImagenMedica()
        imagenMedica.url_imagen = dto.url_imagen
        # imagenMedica.tipoArchivo = TipoArchivo(dto.tipoArchivo.nombres, dto.tipoArchivo.extension)
        # imagenMedica.archivo = Archivo(dto.archivo.identificador, dto.archivo.ruta)
        # imagenMedica.diagnostico = Diagnostico(dto.diagnostico.fecha_creacion, dto.diagnostico.fecha_actualizacion,
        #                              dto.diagnostico.id)
        # imagenMedica.diagnostico.patologia = Patologia(dto.diagnostico.patologia.nombre)
        # imagenMedica.diagnostico.modalidad = Modalidad(dto.diagnostico.modalidad.nombre)
        # imagenMedica.diagnostico.etiqueta = Etiqueta(dto.diagnostico.etiqueta.identificador)
        
        return imagenMedica



