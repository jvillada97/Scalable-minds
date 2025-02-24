import uuid
import app.seedwork.presentacion.api as api
import json
from app.modulos.imagen_medica.aplicacion.servicios import ServicioImagenMedica
from app.modulos.imagen_medica.aplicacion.dto import ImagenMedicaDTO
from app.seedwork.dominio.excepciones import ExcepcionDominio
from werkzeug.utils import secure_filename
from flask import redirect, render_template, request, session, url_for
from flask import Response, send_file
from app.modulos.imagen_medica.aplicacion.mapeadores import MapeadorImagenMedicaDTOJson
from app.modulos.imagen_medica.aplicacion.comandos.crear_imagen_medica import CrearImagenMedica
from app.modulos.imagen_medica.aplicacion.queries.obtener_todas_imagen_medicas import ObtenerTodasImagenesMedicas
import os
import io
import mimetypes
import zipfile
from app.seedwork.aplicacion.queries import ejecutar_query
from app.seedwork.aplicacion.comandos import ejecutar_commando

bp = api.crear_blueprint('imagen-medica', '/imagen-medica')


@bp.route('/', methods=('POST',))
def imagenMedica():
    try:        
        archivo_imagen = request.files.get('archivo_imagen')   
        
        filename = secure_filename(archivo_imagen.filename)
        save_path = os.path.join('src', 'images', filename)
        print(save_path)
        
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        archivo_imagen.save(save_path)
        
        comando = CrearImagenMedica(
            url_image=save_path,
        )
        ejecutar_commando(comando)
        return {"message": "Imagen médica creada exitosamente"}, 201
    
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/', methods=('GET',))
def dar_imnagenes_medicas():
    try:
        map_propiedad = MapeadorImagenMedicaDTOJson()
        query_resultado = ejecutar_query(ObtenerTodasImagenesMedicas())
        resultados = []
        
        for propiedad in query_resultado.resultado:
            resultados.append(map_propiedad.dto_a_externo(propiedad))    
        
        print(resultados)
        rutas_archivos = [item["url_imagen"] for item in resultados if "url_imagen" in item]

        if not rutas_archivos:
            return Response(json.dumps(dict(error="No se proporcionaron archivos válidos")), status=400, mimetype="application/json")
        
        print(rutas_archivos)
        zip_buffer = io.BytesIO()

        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for ruta in rutas_archivos:
                ruta_real = os.path.abspath(ruta)  # Convierte la ruta a absoluta

                if os.path.exists(ruta_real):
                    zip_file.write(ruta_real, os.path.basename(ruta_real))
                else:
                    print(f"Archivo no encontrado: {ruta_real}")

            # Enviar el ZIP como respuesta
        zip_buffer.seek(0)
        return send_file(zip_buffer, mimetype='application/zip', as_attachment=True, download_name="archivos.zip")
   
    except Exception as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    

@bp.route('/imagen-medica/<path:url_imagen>', methods=('GET',))
def obtener_imagen(url_imagen):
    try:
        mimetype, _ = mimetypes.guess_type(url_imagen)
        if not mimetype:
            mimetype = "application/octet-stream"
            
        return send_file(url_imagen, mimetype='image/jpeg')
    except Exception as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    
@bp.route("/ping")
def health():
    return {"status": "pong"}