from flask import Flask
from routes.leituras import leituras_bp
from routes.sensores import sensores_bp

app = Flask(__name__)

@app.registrar_blueprint(leituras_bp)
@app.registrar_blueprint(sensores_bp)

@app.route("/")
def index():
    return "Dashboard funcionando!"

if __name__ == "__main__":
    ## porta 5000 no servidor
    app.run(debug = True)