import os
from flask import Flask, render_template, request, redirect

#EXPLANATION:
# HI, THIS IS JUST A FORMULARY, DON´T ASK FOR IT
base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, template_folder=os.path.join(base_dir, 'templates'))

Global_Formula = {
    "Matematica": {
        "derivadas": [
    {"id": 1, "nombre": "Derivada de una constante", "formula": "d/dx [c] = 0"},
    {"id": 2, "nombre": "Derivada de la variable x", "formula": "d/dx [x] = 1"},
    {"id": 3, "nombre": "Derivada de una potencia", "formula": "d/dx [x^n] = n * x^(n-1)"},
    {"id": 4, "nombre": "Regla del producto", "formula": "d/dx [f * g] = f' * g + f * g'"},
    {"id": 5, "nombre": "Regla del cociente", "formula": "d/dx [f / g] = (f' * g - f * g') / g^2"},
    {"id": 6, "nombre": "Regla de la cadena", "formula": "d/dx [f(g(x))] = f'(g(x)) * g'(x)"},
    {"id": 7, "nombre": "Derivada de la función exponencial e^x", "formula": "d/dx [e^x] = e^x"},
    {"id": 8, "nombre": "Derivada del logaritmo natural ln(x)", "formula": "d/dx [ln(x)] = 1/x"},
    {"id": 9, "nombre": "Derivada del seno", "formula": "d/dx [sin(x)] = cos(x)"},
    {"id": 10, "nombre": "Derivada del coseno", "formula": "d/dx [cos(x)] = -sin(x)"}
        ],
        "integrales": [
    {"id": 1, "nombre": "Integral de una constante", "formula": "S c dx = c * x + C"},
    {"id": 2, "nombre": "Integral de una potencia", "formula": "S x^n dx = (x^(n+1)) / (n+1) + C  (n != -1)"},
    {"id": 3, "nombre": "Integral reciproca (Logarítmica)", "formula": "S (1/x) dx = ln(|x|) + C"},
    {"id": 4, "nombre": "Integral exponencial e^x", "formula": "S e^x dx = e^x + C"},
    {"id": 5, "nombre": "Integral por partes", "formula": "S u dv = u * v - S v du"},
    {"id": 6, "nombre": "Integral del seno", "formula": "S sin(x) dx = -cos(x) + C"},
    {"id": 7, "nombre": "Integral del coseno", "formula": "S cos(x) dx = sin(x) + C"},
    {"id": 8, "nombre": "Integral de la secante cuadrada (Tangente)", "formula": "S sec^2(x) dx = tan(x) + C"},
    {"id": 9, "nombre": "Integral directa para Arcotangente", "formula": "S (1 / (a^2 + x^2)) dx = (1/a) * arctan(x/a) + C"},
    {"id": 10, "nombre": "Integral directa para Arcoseno", "formula": "S (1 / sqrt(a^2 - x^2)) dx = arcsin(x/a) + C"}
        ]
    },
    "Fisica": {
        "resistores": [
            {"id": 1, "nombre": "Resistores en Serie", "formula": "R_eq = R1 + R2 + ... + Rn"},
            {"id": 2, "nombre": "Resistores en Paralelo", "formula": " 1/R_eq = 1/R1 + 1/R2 + ... + 1/Rn"}
        ],
        "campo_gravitacional": [
            {"id": 1, "nombre": "Ley de Gravitación Universal", "formula": "F = G * (m1 * m2) / r^2"},
            {"id": 2, "nombre": "Intensidad de Campo Gravitatorio", "formula": "g = G * M / r^2"}
        ]
        , 
        "ley_kirchhoff": [
            {"id": 1, "nombre": "Primera Ley (Nodos)", "formula": "S I_entrada = S I_salida"},
            {"id": 2, "nombre": "Segunda Ley (Mallas)", "formula": "S V = 0"}
        ],
        "capacitores": [
            {"id": 1, "nombre": "Capacitores en Paralelo", "formula": "C_eq = C1 + C2 + ... + Cn"},
            {"id": 2, "nombre": "Capacitores en Serie", "formula": "1/C_eq = 1/C1 + 1/C2 + ... + 1/Cn"}
        ],   
    },
    "Quimica": {
        "Molaridad": [
            {"id": 1, "nombre": "Molaridad (M)", "formula": "M = moles de soluto / litros de solución"},
            {"id": 2, "nombre": "Moles desde Masa", "formula": "n = masa (g) / peso molecular (g/mol)"}
        ],
        "Molalidad": [
            {"id": 1, "nombre": "Molalidad (m)", "formula": "m = moles de soluto / kg de solvente"}
        ],
        "%V/V": [
            {"id": 1, "nombre": "Porcentaje Volumen/Volumen (%V/V)", "formula": "%V/V = (volumen soluto / volumen solución) * 100"}
        ],
        "%M/V": [
            {"id": 1, "nombre": "Porcentaje Masa/Volumen (%M/V)", "formula": "%M/V = (gramos soluto / mL solución) * 100"}
        ],
        "%M/M": [
            {"id": 1, "nombre": "Porcentaje Masa/Masa (%M/M)", "formula": "%M/M = (masa soluto / masa solución) * 100"}
        ],        
    },
    "Probabilidad": {
        "Distribuciones": {
            "Distribución Binomial": [
                {"id": 1, "nombre": "Función de Probabilidad Binomial", "formula": "P(X = x) = nCx * p^x * q^(n-x)"},
                {"id": 2, "nombre": "Media de Binomial", "formula": "mu = n * p"}
            ],
            "Distribución Geométrica": [
                {"id": 1, "nombre": "Función de Probabilidad Geométrica", "formula": "P(X = x) = q^(x-1) * p"},
                {"id": 2, "nombre": "Media de Geométrica", "formula": "mu = 1 / p"}
            ],
            "Distribución de Poisson": [
                {"id": 1, "nombre": "Función de Probabilidad de Poisson", "formula": "P(X = x) = (e^(-l) * l^x) / x!"},
                {"id": 2, "nombre": "Varianza de Poisson", "formula": "sigma^2 = l"}
            ],
            "Distribución HiperGeométrica": [
                {"id": 1, "nombre": "Función Hipergeométrica", "formula": "P(X = x) = (kCx * (N-k)C(n-x)) / NCn"}
            ],
            "Distribución Multinomial": [
                {"id": 1, "nombre": "Función de Probabilidad Multinomial", "formula": "P = (n! / (x1! * x2! * ... * xk!)) * p1^x1 * p2^x2 * ... * pk^xk"}
            ]
        },
        "Variables Aleatorias": {
            "Variable_Aleatoria_Discreta": [
                {"id": 1, "nombre": "Esperanza Matemática E(X)", "formula": "E(X) = S [ x * P(X = x) ]"},
                {"id": 2, "nombre": "Varianza sigma^2", "formula": "Var(X) = E(X^2) - [E(X)]^2"}
            ],
            "Variable_Aleatoria_Continua": [
                {"id": 1, "nombre": "Condición de Normalización", "formula": "S_{-inf}^{inf} f(x) dx = 1"},
                {"id": 2, "nombre": "Esperanza Matemática E(X)", "formula": "E(X) = S_{-inf}^{inf} x * f(x) dx"}
            ]
        }
    }
}

@app.route("/")
def home():
    return "BUENAS, ESTE ES UN FORMULARIO GLOBAL :D"

@app.route("/formulario/matematica/<tema>")
def formulario_matematica(tema):
    lista_formulas = Global_Formula["Matematica"][tema]
    return render_template("render.html", formulas = lista_formulas, materia = "Matematica", tema = tema)

@app.route("/formulario/fisica/<tema>")
def formulario_fisica(tema):
    lista_formulas = Global_Formula["Fisica"][tema]
    return render_template("render.html", formulas = lista_formulas, materia = "Fisica", tema = tema)

@app.route("/formulario/quimica/<tema>")
def formulario_quimica(tema):
    lista_formulas = Global_Formula["Quimica"][tema]
    return render_template("render.html", formulas = lista_formulas, materia = "Quimica", tema = tema)

@app.route("/formulario/probabilidad/<subgrupo>/<tema>")
def formulario_probabilidad(sub_grupo, tema):
    lista_formulas = Global_Formula["Quimica"][sub_grupo][tema]
    return render_template("render.html", formulas = lista_formulas, materia = "Quimica", sub_grupo = sub_grupo, tema = tema)

@app.route("/resolver/matematica/<tema>",methods=["POST"])
def resolver_matematica(tema):
    lista = Global_Formula["Matematica"][tema]
    nueva_formula = {"id": len(lista) + 1, "nombre": request.form.get("nombre"), "formula": request.form.get("formula")}
    lista.append(nueva_formula)
    return redirect(f"/formulario/matematica/{tema}")

@app.route("/resolver/fisica/<tema>", methods=["POST"])
def resolver_fisica(tema):
    lista = Global_Formula["Fisica"][tema]
    nueva_formula = {"id": len(lista) + 1, "nombre": request.form.get("nombre"), "formula": request.form.get("formula")}
    lista.append(nueva_formula)
    return redirect(f"/formulario/fisica/{tema}")

@app.route("/resolver/quimica/<tema>", methods=["POST"])
def resolver_quimica(tema):
    lista = Global_Formula["Quimica"][tema]
    nueva_formula = {"id": len(lista) + 1, "nombre": request.form.get("nombre"), "formula": request.form.get("formula")}
    lista.append(nueva_formula)
    return redirect(f"/formulario/quimica/{tema}")

@app.route("/resolver/probabilidad/<sub_grupo>/<tema>", methods=["POST"])
def resolver_probabilidad(sub_grupo, tema):
    lista = Global_Formula["Probabilidad"][sub_grupo][tema]
    nueva_formula = {"id": len(lista) + 1, "nombre": request.form.get("nombre"), "formula": request.form.get("formula")}
    lista.append(nueva_formula)
    return redirect(f"/formulario/probabilidad/{sub_grupo}/{tema}")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
  
  

