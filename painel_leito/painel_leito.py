"""Modulo para gerenciamento do painel do leito hospitalar."""
import requests
import utils.loadinfo

environment_vars = utils.loadinfo.environment_vars()


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
        response = requests.get(f'{environment_vars["sinais_vitais_container_protocol"]}'
                                f'://{environment_vars["sinais_vitais_container_name"]}'
                                f':{environment_vars["sinais_vitais_container_port"]}'
                                f'/status',
                                timeout=5)

        self.dados_leito.update(response.json())


    def get_data_bomba_infusao(self):
        response = requests.get(f'{environment_vars["bomba_infusao_container_protocol"]}'
                                f'://{environment_vars["bomba_infusao_container_name"]}'
                                f':{environment_vars["bomba_infusao_container_port"]}'
                                f'/status',
                                timeout=5)
        self.dados_leito.update(response.json())

    def get_data_respirador(self):
        response = requests.get(f'{environment_vars["respirador_container_protocol"]}'
                                f'://{environment_vars["respirador_container_name"]}'
                                f':{environment_vars["respirador_container_port"]}'
                                f'/status',
                                timeout=5)
        self.dados_leito.update(response.json())

    def get_data_cardioversor(self):
        response = requests.get(f'{environment_vars["cardioversor_container_protocol"]}'
                                f'://{environment_vars["cardioversor_container_name"]}'
                                f':{environment_vars["cardioversor_container_port"]}'
                                f'/status',
                                timeout=5)
        self.dados_leito.update(response.json())
        self.dados_leito["cardioversor"]["freq_cardiaca"]=self.dados_leito["sinais_vitais"]["freq_cardiaca"]

    def get_data_botao_emergencia(self):
        response = requests.get(f'{environment_vars["botao_emergencia_container_protocol"]}'
                                f'://{environment_vars["botao_emergencia_container_name"]}'
                                f':{environment_vars["botao_emergencia_container_port"]}'
                                f'/status',
                                timeout=5)
        self.dados_leito.update(response.json())
