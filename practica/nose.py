
import json
import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


DATA_FILE = 'formulas.json'

def cargar_datos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return { "Matematica": {}, "Fisica": {}, "Quimica": {}, "Probabilidad": {} }

def guardar_datos(datos):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

Global_Formula = cargar_datos()

# -pene-
@app.route("/resolver/<materia>/<tema>", methods=["POST"])
def resolver_general(materia, tema):
    
    materia_key = materia.capitalize() 
    
    if materia_key in Global_Formula and tema in Global_Formula[materia_key]:
        lista = Global_Formula[materia_key][tema]
        
        
        nuevo_id = lista[-1]['id'] + 1 if lista else 1
        
        nueva_f = {
            "id": nuevo_id,
            "nombre": request.form.get("nombre"),
            "formula": request.form.get("formula")
        }
        
        lista.append(nueva_f)
        guardar_datos(Global_Formula) 
        
    return redirect(f"/formulario/{materia}/{tema}")


