from app.seedwork.aplicacion.dto import Mapeador as AppMap
from app.seedwork.dominio.repositorios import Mapeador as RepMap
from app.modulos.anonimizacion.dominio.entidades import Anonimizacion, Diagnostico
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
           

    def dto_a_entidad(self, dto: AnonimizacionDTO) -> Anonimizacion:
        Anonimizacion = Anonimizacion()
        Anonimizacion.url_imagen = dto.url_imagen
        # Anonimizacion.tipoArchivo = TipoArchivo(dto.tipoArchivo.nombres, dto.tipoArchivo.extension)
        # Anonimizacion.archivo = Archivo(dto.archivo.identificador, dto.archivo.ruta)
        # Anonimizacion.diagnostico = Diagnostico(dto.diagnostico.fecha_creacion, dto.diagnostico.fecha_actualizacion,
        #                              dto.diagnostico.id)
        # Anonimizacion.diagnostico.patologia = Patologia(dto.diagnostico.patologia.nombre)
        # Anonimizacion.diagnostico.modalidad = Modalidad(dto.diagnostico.modalidad.nombre)
        # Anonimizacion.diagnostico.etiqueta = Etiqueta(dto.diagnostico.etiqueta.identificador)
        
        return Anonimizacion



