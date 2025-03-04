from app.seedwork.aplicacion.dto import Mapeador as AppMap
from app.seedwork.dominio.repositorios import Mapeador as RepMap
from app.modulos.proveedor.dominio.entidades import Proveedor
from app.modulos.proveedor.dominio.objetos_valor import TipoArchivo, Archivo, Patologia, Modalidad, Etiqueta
from app.modulos.proveedor.aplicacion.dto import ProveedorDTO
from werkzeug.datastructures import FileStorage
from dataclasses import field 
from datetime import datetime

class MapeadorProveedorDTOJson(AppMap):   
    
    def externo_a_dto(self, externo: dict) -> ProveedorDTO:
         return ProveedorDTO(
            name=externo.get('name')
        )


    def dto_a_externo(self, dto: ProveedorDTO) -> dict:
        return dto.__dict__
    
class MapeadorProveedor(RepMap):

    def obtener_tipo(self) -> type:        
        return Proveedor.__class__


    def entidad_a_dto(self, entidad: Proveedor) -> ProveedorDTO:
        compania_dto = ProveedorDTO()
        compania_dto.name = entidad.name       
        return compania_dto
           

    def dto_a_entidad(self, dto: ProveedorDTO) -> Proveedor:
        proveedor = Proveedor()
        proveedor.name = dto.name              
        return proveedor



