from services.leitura_service import LeituraService

class LeituraController:
    @staticmethod
    def processar_calculo(dados):
        vol = dados.get('volume')
        temp = dados.get('tempo')
        
        if vol is None or temp is None:
            return {"erro": "Dados incompletos"}, 400
            
        resultado = LeituraService.calcular_vazao(vol, temp)
        return {"vazao": resultado}, 200