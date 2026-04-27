from flask import Blueprint, request, jsonify
from db.connection import Autenticar

login_bp = Blueprint('login', __name__)
@login_bp.route("/login", methods=["POST"])
def login():
    dados = request.get_json()
    print(f"DEBUG: Recebi no Flask -> {dados}")
    usuario = dados.get("usuario")
    senha = dados.get("senha")

    auth = Autenticar()
    if auth.verificar_login(usuario, senha):
        return jsonify({"mensagem": "Login aprovado!"}), 200
    
    return jsonify({"erro": "Usuário ou senha incorretos"}), 401