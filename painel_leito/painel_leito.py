"""Modulo para gerenciamento do painel do leito hospitalar."""
import requests
class PainelDoLeito:
    """
    Classe para gerenciamento do painel do leito hospitalar
    """
    def __init__(self):
        """
        Metodo para inicializar os atributos do leito hospitalar
        """
        self.dados_leito = {}

    def get_data_sinais_vitais(self):
        """Obtém o status da Bomba de Infusão"""
        response = requests.get("http://10.0.0.254:7001/sinais_vitais", timeout=5)
        self.dados_leito.update(response.json())

    def get_data_bomba_infusao(self):
        """Obtém o status da Bomba de Infusão"""
        response = requests.get("http://10.0.0.254:7002/status", timeout=5)
        self.dados_leito.update(response.json())

    def get_data_respirador(self):
        """Obtém o status da Bomba de Infusão"""
        response = requests.get("http://10.0.0.254:7003/status", timeout=5)
        self.dados_leito.update(response.json())

    def get_data_cardioversor(self):
        """Obtém o status da Bomba de Infusão"""
        response = requests.get("http://10.0.0.254:7004/status", timeout=5)
        self.dados_leito.update(response.json())

    def get_data_botao_emergencia(self):
        """Obtém o status da Bomba de Infusão"""
        response = requests.get("http://10.0.0.254:7005/status", timeout=5)
        self.dados_leito.update(response.json())


paine = PainelDoLeito()
paine.get_data_sinais_vitais()
paine.get_data_bomba_infusao()
paine.get_data_respirador()
paine.get_data_botao_emergencia()
paine.get_data_cardioversor()

print(paine.dados_leito)
