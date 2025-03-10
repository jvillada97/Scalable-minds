from aplicacion.dto import ProveedorDTO


class MapeadorProveedorDTOJson():
    def externo_a_dto(self, externo: dict) -> ProveedorDTO:
        proveedor_dto = ProveedorDTO()
        proveedor_dto.name = externo.get('name')          
        return proveedor_dto
    
    def dto_a_externo(self, dto: ProveedorDTO) -> dict:
        return dto.__dict__