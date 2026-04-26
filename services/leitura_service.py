class Calcular_Vazao:

    @staticmethod
    def calcular(volume, tempo):
        if tempo == 0:
            return "Erro: O tempo tem que ser diferente de zero."
        vazao = volume / tempo
        return vazao
    
if __name__ == "__main__":

    v = Calcular_Vazao()
    resultado = v.calcular(100,10)
    print(f"O valor da vazão é: {resultado}")