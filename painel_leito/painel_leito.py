import requests
# from fastapi import Request

class PainelDoLeito:
    def __init__(self): 
        self.dados_leito = {}

    def get_data_sinais_vitais(self):
        # Obtém o status da Bomba de Infusão
        response = requests.get("http://10.0.0.254:7001/sinais_vitais")
        self.dados_leito.update(response.json())
    
    def get_data_bomba_infusao(self):
        # Obtém o status da Bomba de Infusão
        response = requests.get("http://10.0.0.254:7002/status")
        self.dados_leito.update(response.json())
    
    def get_data_respirador(self):
        # Obtém o status da Bomba de Infusão
        response = requests.get("http://10.0.0.254:7003/status")
        self.dados_leito.update(response.json())

    def get_data_cardioversor(self):
        # Obtém o status da Bomba de Infusão
        response = requests.get("http://10.0.0.254:7004/status")
        self.dados_leito.update(response.json())

    def get_data_botao_emergencia(self):
        # Obtém o status da Bomba de Infusão
        response = requests.get("http://10.0.0.254:7005/status")
        self.dados_leito.update(response.json())
    
    
paine = PainelDoLeito()
paine.get_data_sinais_vitais()
paine.get_data_bomba_infusao()
paine.get_data_respirador()
paine.get_data_botao_emergencia()
paine.get_data_cardioversor()

print(paine.dados_leito)