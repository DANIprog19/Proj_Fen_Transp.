from flask import Flask, render_template
from rotas.leituras import leituras_bp
from rotas.sensores import sensores_bp
from rotas.login import login_bp

app = Flask(__name__)

# REGISTROS DEVEM FICAR AQUI (FORA DE QUALQUER FUNÇÃO OU IF)
app.register_blueprint(sensores_bp, url_prefix='/sensores')
app.register_blueprint(leituras_bp, url_prefix='/leituras')
app.register_blueprint(login_bp) # SEM prefixo

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    # O print das rotas para termos certeza absoluta:
    with app.app_context():
        print("\n--- VERIFICANDO ROTAS ---")
        for rule in app.url_map.iter_rules():
            print(f"URL: {rule.rule} -> Endpoint: {rule.endpoint}")
        print("--------------------------\n")
    
    app.run(debug=True)