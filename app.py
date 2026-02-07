from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
        mensaje = "Cuidar el planeta es cuidar nuestra vida"
        return render_template('index.html', breadcrumb=[""], mensaje=mensaje)


@app.route('/sistema', methods=['GET', 'POST'])
def sistema():
    acciones = []
    if request.method == 'POST':
        acciones = request.form.getlist('acciones')
    return render_template('sistema.html', breadcrumb=["Inicio", "Sistema Ambiental"], acciones=acciones)

@app.route('/ubicacion')
def ubicacion():
    # Coordenadas estratégicas de Dolores Hidalgo
    recicladoras = [
        {"nombre": "Recicladora El Relicario", "lat": 21.1685, "lon": -100.9210, "tipo": "Metales", "info": "Cerca de la salida a San Luis"},
        {"nombre": "Centro de Acopio Ecofila", "lat": 21.1450, "lon": -100.9420, "tipo": "Plásticos", "info": "Col. Lindavista"},
        {"nombre": "Papelera Hidalgo", "lat": 21.1580, "lon": -100.9350, "tipo": "Papel/Cartón", "info": "Zona Centro"},
        {"nombre": "Depósito La Cuna", "lat": 21.1720, "lon": -100.9150, "tipo": "Chatarra", "info": "A pie de carretera"}
    ]
    return render_template('mapa.html', breadcrumb=["Ubicación"], recicladoras=recicladoras)


@app.route('/futuro', methods=['GET', 'POST'])
def futuro():
    escenario = None
    if request.method == 'POST':
        escenario = request.form.get('decision')
    return render_template('futuro.html', breadcrumb=["Inicio", "Futuro"], escenario=escenario)


@app.route('/tres-r')
def tres_r():
    return render_template('tres_r.html', breadcrumb=["Inicio", "Las 3 R"])


if __name__ == '__main__':
    # host='0.0.0.0' permite conexiones de otros dispositivos
    app.run(debug=True, host='0.0.0.0', port=5000)