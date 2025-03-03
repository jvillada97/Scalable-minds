from dataclasses import dataclass
from app.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from app.seedwork.aplicacion.queries import ejecutar_query as query
from app.modulos.proveedor.dominio.entidades import Proveedor
from app.modulos.proveedor.aplicacion.queries.base import ProveedorQueryBaseHandler
from app.modulos.proveedor.aplicacion.mapeadores import MapeadorProveedor
from app.modulos.proveedor.aplicacion.dto import ProveedorDTO

@dataclass
class ObtenerTodosProveedores(Query):
    ...

class ObtenerTodosProveedoresHandler(ProveedorQueryBaseHandler):

    def handle(self, query) -> QueryResultado:
        propiedades_dto = []
        vista = self._fabrica_vista.crear_objeto(Proveedor)
        propiedades = vista.obtener_todos()    

        for propiedad in propiedades:
            dto = ProveedorDTO(
                url_imagen=propiedad.url_imagen
                )
            propiedades_dto.append(dto)    
        
        return QueryResultado(resultado=propiedades_dto)

@query.register(ObtenerTodosProveedores)
def ejecutar_query_obtener_propiedad(query: ObtenerTodosProveedores):
    handler = ObtenerTodosProveedoresHandler()
    return handler.handle(query)