from services.leitura_service import LeituraService

class LeituraController:

    @staticmethod
    def processar_calculo(dados):
        vol = dados.get("volume")
        temp = dados.get("tempo")

        resultado = LeituraService.calcular_vazao(vol, temp)
        print("RESULTADO:", resultado)

        return resultado, 200