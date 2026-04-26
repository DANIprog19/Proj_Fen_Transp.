import sqlite3


class Autenticar:
    def __init__(self, banco= 'banco_dados.db'):
        self.banco = banco

    def verificar_login(self, usuario_digitado, senha_digitada):
        conexao = sqlite3.connect(self.banco)
        cursor = conexao.cursor()

        query = "SELECT senha FROM usuarios WHERE usuario = ?"
        cursor.execute(query, (usuario_digitado,))
        resultado = cursor.fetchone()

        conexao.close()

        if resultado:
            senha_gravada = resultado[0]
            if str(senha_gravada) == str(senha_digitada):
                print("Acesso concedido!")
                return True
            else:
                print("Senha Incorreta!")
                return False
        else:
            print("Usuário não encontrado!")
            return False

        

