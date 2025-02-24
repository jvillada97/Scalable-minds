import uuid
import app.seedwork.presentacion.api as api
import json
from app.modulos.imagen_medica.aplicacion.servicios import ServicioImagenMedica
from app.modulos.imagen_medica.aplicacion.dto import ImagenMedicaDTO
from app.seedwork.dominio.excepciones import ExcepcionDominio
from werkzeug.utils import secure_filename
from flask import redirect, render_template, request, session, url_for
from flask import Response
from app.modulos.imagen_medica.aplicacion.mapeadores import MapeadorImagenMedicaDTOJson
from app.modulos.imagen_medica.aplicacion.comandos.crear_imagen_medica import CrearImagenMedica
from app.modulos.imagen_medica.aplicacion.queries.obtener_todas_imagen_medicas import ObtenerTodasImagenesMedicas
import os
from app.seedwork.aplicacion.queries import ejecutar_query
from app.seedwork.aplicacion.comandos import ejecutar_commando

bp = api.crear_blueprint('imagen-medica', '/imagen-medica')


@bp.route('/imagen-medica', methods=('POST',))
def imagenMedica():
    try:
        print("Paso 1")
        
        archivo_imagen = request.files.get('archivo_imagen')   
        print(f"Archivo Imagen: {archivo_imagen.filename}")
        
        filename = secure_filename(archivo_imagen.filename)
        save_path = os.path.join('src', 'images', filename)
        print(save_path)
        
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        archivo_imagen.save(save_path)
        
        comando = CrearImagenMedica(
            url_image=save_path,
        )
        ejecutar_commando(comando)
    
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/imagen-medica', methods=('GET',))
def dar_imnagenes_medicas():
    map_propiedad = MapeadorImagenMedicaDTOJson()
    query_resultado = ejecutar_query(ObtenerTodasImagenesMedicas())
    resultados = []
    
    for propiedad in query_resultado.resultado:
        resultados.append(map_propiedad.dto_a_externo(propiedad))
    
    return resultados
    
@bp.route("/ping")
def health():
    return {"status": "pong"}