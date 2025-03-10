import requests
from flask import request
import os
import json 


def crear_proveedor(dto):
    url= f"{os.getenv('HOST_PROVEEDOR')}/proveedor" 
    data = {
        "name": dto.name,
    }
    headers = {"Content-Type": "application/json"}
    try:
        print(url)
        print(data)
        response = requests.post(url, json=data, headers=headers)        
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
   
