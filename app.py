from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
        mensaje = "Cuidar el planeta es cuidar nuestra vida"
        return render_template('index.html', breadcrumb=["Inicio"], mensaje=mensaje)


@app.route('/sistema', methods=['GET', 'POST'])
def sistema():
    acciones = []
    if request.method == 'POST':
        acciones = request.form.getlist('acciones')
    return render_template('sistema.html', breadcrumb=["Inicio", "Sistema Ambiental"], acciones=acciones)


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
    app.run(debug=True)