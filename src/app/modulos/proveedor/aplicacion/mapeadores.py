from app.seedwork.aplicacion.dto import Mapeador as AppMap
from app.seedwork.dominio.repositorios import Mapeador as RepMap
from app.modulos.proveedor.dominio.entidades import Proveedor
from app.modulos.proveedor.aplicacion.dto import ProveedorDTO

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
        return ProveedorDTO(
            name=entidad.name
        )

    def dto_a_entidad(self, dto: ProveedorDTO) -> Proveedor:
        print(dto)
        proveedor = Proveedor()
        proveedor.name = dto.name              
        return proveedor