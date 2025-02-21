from dataclasses import dataclass, field
from app.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class TipoArchivoDTO(DTO):
    nombres: str
    extension: str

@dataclass(frozen=True)
class ArchivoDTO(DTO):
    identificador: str
    ruta: str
    
@dataclass(frozen=True)
class EtiquetaDTO(DTO):
    identificador: str    
    
@dataclass(frozen=True)
class ModalidadDTO(DTO):
    nombre: str    
    
@dataclass(frozen=True)
class PatologiaDTO(DTO):
    nombre: str    
    
@dataclass(frozen=True)
class DiagnosticoDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)
    etiqueta: EtiquetaDTO = field(default_factory=list)
    modalidad: ModalidadDTO = field(default_factory=list)
    patologia: PatologiaDTO = field(default_factory=list)
    
@dataclass(frozen=True)
class ImagenMedicaDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)
    tipoArchivo: TipoArchivoDTO = field(default_factory=list)
    archivo: ArchivoDTO = field(default_factory=list)
    diagnostico: DiagnosticoDTO = field(default_factory=list)