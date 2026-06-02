from flask import Flask, render_template, request, redirect

app = Flask(__name__)

my_items = [
   {"id": 1, "expresion": "1 / (sin(t) + cos(t))", "metodo": "Sustitucion de Weirstrass", "tipo": "díficil","solución": "(sqrt(2) / 2) * ln(|tan(t/2) - 1 + sqrt(2) / (sqrt(2) / 2) ) ! * ln(|tan(t/2) - 1 + sqrt(2)) !) + C"},
   {"id": 2, "expresion": "x * e^x", "metodo": "Aventura", "tipo": "maso", "solución": "x * e^x - e^x + C"},
   {"id": 3, "expresion": "ln(x) / x", "metodo": "Cambio de variable", "tipo": "isi","solución": "(1/2) * (ln(x))^2 + C"},
   {"id": 4, "expresion": "3x^2 + 5x - 2", "metodo": "Directa", "tipo": "meh","solución": "x^3 + (5/2) x^2 - 2x + C"},
   {"id": 5, "expresion": "dx / 81 + x^2", "metodo": "Directa - Arcotangente", "tipo": "facil", "solución": "(1/9) * arctan(1/9) + C"}
]

proximo_id = 6

@app.route("/")
def home():
    return "Hola, esta es mi lista de integrales pa que te traumes :D"

@app.route("/integrales")
def mostrar_integrales():
    print("LISTA DO INTEGRALES (LOL)")
    for item in my_items:
        print(f"ID: {item['id']} | Expresión: {item['expresion']} | Solución: {item['solución']}")
    return render_template("work.html", integrales = my_items)

def agregar_integrales(expresión, metodo, tipo, solución):
    global proximo_id

    nuevo_ejercicio = {
        "id": proximo_id,
        "expresion": expresión,
        "metodo": metodo,
        "tipo": tipo,
        "solución": solución
    }

    my_items.append(nuevo_ejercicio)
    print(f"Listo, se guardó la integral")

    proximo_id += 1
        
@app.route("/resolver", methods=["POST"])
def integrales():
    expresion_input = request.form.get("expresion")
    metodo_input = request.form.get("metodo")
    tipo_input = request.form.get("tipo")
    solucion_input = request.form.get("solucion")

    agregar_integrales(expresion_input, metodo_input, tipo_input, solucion_input)

    return redirect("/integrales")

if __name__ == "__main__":
    app.run(debug = True, port = 8000)

