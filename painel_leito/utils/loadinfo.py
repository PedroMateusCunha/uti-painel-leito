#!/bin/usr/python3
""" Module with all load data utilities """

import os

def environment_vars() -> dict:
    """ Load all environment variables needed """
    return { "botao_emergencia_container_name": os.getenv('BOTAO_EMERGENCIA_CONTAINER_NAME'),
             "botao_emergencia_container_port": os.getenv('BOTAO_EMERGENCIA_CONTAINER_PORT'),
             "botao_emergencia_container_protocol": os.getenv('BOTAO_EMERGENCIA_CONTAINER_PROTOCOL'),
             
             "cardioversor_container_name": os.getenv('CARDIOVERSOR_CONTAINER_NAME'),
             "cardioversor_container_port": os.getenv('CARDIOVERSOR_CONTAINER_PORT'),
             "cardioversor_container_protocol": os.getenv('CARDIOVERSOR_CONTAINER_PROTOCOL'),
             
             "sinais_vitais_container_name": os.getenv('SINAIS_VITAIS_CONTAINER_NAME'),
             "sinais_vitais_container_port": os.getenv('SINAIS_VITAIS_CONTAINER_PORT'),
             "sinais_vitais_container_protocol": os.getenv('SINAIS_VITAIS_CONTAINER_PROTOCOL'),
             
             "painel_leito_container_name": os.getenv('PAINEL_LEITO_CONTAINER_NAME'),
             "painel_leito_container_port": os.getenv('PAINEL_LEITO_CONTAINER_PORT'),
             "painel_leito_container_protocol": os.getenv('PAINEL_LEITO_CONTAINER_PROTOCOL'),
             
             "respirador_container_name": os.getenv('RESPIRADOR_CONTAINER_NAME'),
             "respirador_container_port": os.getenv('RESPIRADOR_CONTAINER_PORT'),
             "respirador_container_protocol": os.getenv('RESPIRADOR_CONTAINER_PROTOCOL'),
             
             "bomba_infusao_container_name": os.getenv('BOMBA_INFUSAO_CONTAINER_NAME'),
             "bomba_infusao_container_port": os.getenv('BOMBA_INFUSAO_CONTAINER_PORT'),
             "bomba_infusao_container_protocol": os.getenv('BOMBA_INFUSAO_CONTAINER_PROTOCOL'),}