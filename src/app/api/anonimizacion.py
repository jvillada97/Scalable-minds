import app.seedwork.presentacion.api as api
import uuid
import app.seedwork.presentacion.api as api
import json
from app.modulos.anonimizacion.aplicacion.servicios import ServicioAnonimizacion
from app.modulos.anonimizacion.aplicacion.dto import AnonimizacionDTO
from app.seedwork.dominio.excepciones import ExcepcionDominio
from werkzeug.utils import secure_filename
from flask import redirect, render_template, request, session, url_for
from flask import Response, send_file
from app.modulos.anonimizacion.aplicacion.mapeadores import MapeadorAnonimizacionDTOJson
from app.modulos.anonimizacion.aplicacion.queries.obtener_todas_anonimizaciones import ObtenerTodasAnonimizaciones
import os
import io
import mimetypes
import zipfile
from app.seedwork.aplicacion.queries import ejecutar_query
from app.seedwork.aplicacion.comandos import ejecutar_commando
bp = api.crear_blueprint('anonimizacion', '/anonimizacion')


@bp.route('/', methods=('GET',))
def dar_anonimizaciones():
    try:
        map_propiedad = MapeadorAnonimizacionDTOJson()
        query_resultado = ejecutar_query(ObtenerTodasAnonimizaciones())
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
    
