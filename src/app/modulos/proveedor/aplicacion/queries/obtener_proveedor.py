
from dataclasses import dataclass
from app.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from app.seedwork.aplicacion.queries import ejecutar_query as query
from app.modulos.proveedor.dominio.entidades import Proveedor
from app.modulos.proveedor.aplicacion.mapeadores import MapeadorProveedor
from app.modulos.proveedor.aplicacion.dto import ProveedorDTO
from .base import ProveedorQueryBaseHandler
 
 
@dataclass
class ObtenerProveedorPorNombre(Query):
    name: str
 
class ObtenerProveedorHandler(ProveedorQueryBaseHandler):    
 
    def handle(self, query) -> QueryResultado:
        vista = self._fabrica_vista.crear_objeto(Proveedor)      
        print(query.name)
        provedor_dto = vista.obtener_por_nombre(name=query.name)     
        if  provedor_dto is None:
            return QueryResultado(resultado=None)
        else:
            proveedor = self.fabrica_proveedor.crear_objeto(provedor_dto, MapeadorProveedor())
            return QueryResultado(resultado=proveedor)
 
 
@query.register(ObtenerProveedorPorNombre)
def ejecutar_query_obtener_proveedor(query: ObtenerProveedorPorNombre):
    handler = ObtenerProveedorHandler()
    return handler.handle(query)