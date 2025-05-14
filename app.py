from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")  # ruta a pagina de inicio
def index():
    return render_template("index.html")



@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = int(request.form["edad"])
        cantidad = int(request.form["cantidad"])
        precio_unitario = 9000
        total_sin_descuento = cantidad * precio_unitario

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        monto_descuento = total_sin_descuento * descuento
        total_final = total_sin_descuento - monto_descuento

        return render_template("ejercicio1.html",
                               nombre=nombre,
                               total=total_sin_descuento,
                               descuento_aplicado=monto_descuento,
                               total_pagar=total_final)
    return render_template("ejercicio1.html")

usuarios = {
    "juan": {"contraseña": "admin", "rol": "administrador"},
    "pepe": {"contraseña": "user", "rol": "usuario"}
}


@app.route("/ejercicio2", methods=["GET", "POST"])
def login():
    mensaje = ""

    if request.method == "POST":
        usuario = request.form["usuario"]
        contraseña = request.form["contraseña"]

        if usuario in usuarios and usuarios[usuario]["contraseña"] == contraseña:
            rol = usuarios[usuario]["rol"]
            if rol == "administrador":
                mensaje = f"Bienvenido administrador {usuario}"
            elif rol == "usuario":
                mensaje = f"Bienvenido usuario {usuario}"
        else:
            mensaje = "Usuario o Contraseña incorrectos"

    return render_template("ejercicio2.html", mensaje=mensaje)





if __name__ == "__main__":
    app.run(debug=True)
