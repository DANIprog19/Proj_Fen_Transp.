import sqlite3
import os

class Autenticar:
    def __init__(self):
        # Pega o caminho absoluto de onde este arquivo (connection.py) está
        caminho_atual = os.path.dirname(os.path.abspath(__file__))
        
        # Sobe um nível (..) para sair da pasta 'db' e chegar na raiz 'backend'
        # onde está o seu arquivo usuarios.db
        self.banco = os.path.join(caminho_atual, '..', 'usuarios.db')

    def verificar_login(self, usuario_digitado, senha_digitada):
        # O 'check_same_thread=False' ajuda a evitar erros no Flask
        conexao = sqlite3.connect(self.banco, check_same_thread=False)
        cursor = conexao.cursor()

        try:
            # O erro acontece aqui porque o banco aberto está vazio
            query = "SELECT senha FROM usuarios WHERE usuario = ?"
            cursor.execute(query, (usuario_digitado,))
            resultado = cursor.fetchone()
            
            if resultado:
                senha_gravada = resultado[0]
                return str(senha_gravada) == str(senha_digitada)
            return False
            
        except sqlite3.OperationalError as e:
            print(f"ERRO CRÍTICO: Tabela não encontrada no caminho {self.banco}")
            return False
        finally:
            conexao.close()