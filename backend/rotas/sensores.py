from flask import Blueprint, request
from controllers.sensores_controllers import SensoresController

sensores_bp = Blueprint('sensores', __name__)

@sensores_bp.route('/', methods=['GET'])
def listar_todos():
    resultado, status = SensoresController.listar_sensores()
    return resultado, status

@sensores_bp.route('/cadastro', methods=['POST'])
def cadastrar():
    dados = request.get_json()
    resultado, status = SensoresController.cadastrar_sensor(dados)
    return resultado, status