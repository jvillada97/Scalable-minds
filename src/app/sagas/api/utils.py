import requests
from flask import request
import os
import json 


def crear_proveedor(name):
    url= f"{os.getenv('HOST_PROVEEDOR')}/proveedor" 
    data = {
        "name": name,
    }
    headers = {"Content-Type": "application/json"}
    try:
        print(url)
        print(data)
        response = requests.post(url, json=data, headers=headers)        
        print(response)
    except Exception:
        return False 
    
def eliminar_proveedor(name):
    url= f"{os.getenv('HOST_PROVEEDOR')}/proveedor/{name}"   
    headers = {"Content-Type": "application/json"}
    try:
        print(url)
        response = requests.delete(url, headers=headers)        
        print(response)
    except Exception:
        return False 
            

def obtener_proveedor(name):
    try:
        url= f"{os.getenv('HOST_PROVEEDOR')}/proveedor/{name}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()  
    except Exception:
        return False   
    
   
def crear_imagen_medica(archivo_imagen):
    url= f"{os.getenv('HOST_IMAGENMEDICA')}/imagen-medica" 
    try:
        files = {'archivo_imagen': (archivo_imagen.filename, archivo_imagen.stream, archivo_imagen.mimetype)}
        response = requests.post(url, files=files)        
        print(url)
        print(response)
        return True 
    except Exception as e:
        print(e)
        return False   
    

def obtener_imagen_medica(name):
    try:
        url= f"{os.getenv('HOST_IMAGENMEDICA')}/imagen-medica/{name}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()  
    except Exception:
        return False   
   