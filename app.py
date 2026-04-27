from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/produccion')
def produccion():
    return render_template('produccion_agricola.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/alianzas')
def alianzas():
    return render_template('alianzas.html')

@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)