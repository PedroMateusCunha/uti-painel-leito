"""
Modulo para inicialização e disponilibilização do serviço
relacionado ao painel do leito hospitalar.
"""
import time
import threading
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
from painel_leito import *
import utils.log
import utils.loadinfo

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

painel = PainelDoLeito()

environment_vars = utils.loadinfo.environment_vars()

def update_painel():
    painel.get_data_sinais_vitais()
    painel.get_data_bomba_infusao()
    painel.get_data_respirador()
    painel.get_data_botao_emergencia()
    painel.get_data_cardioversor()

update_painel()

def update_context():
    return {"taxa_med1": painel.dados_leito["bomba_infusao"]["taxas"]["med1"],
            "taxa_med2": painel.dados_leito["bomba_infusao"]["taxas"]["med2"],
            "taxa_soro": painel.dados_leito["bomba_infusao"]["taxas"]["soro"],
            "qtd_med1": painel.dados_leito["bomba_infusao"]["quantidades"]["med1"],
            "qtd_med2": painel.dados_leito["bomba_infusao"]["quantidades"]["med2"],
            "qtd_soro": painel.dados_leito["bomba_infusao"]["quantidades"]["soro"],
            "bomba_infusao_ligado": painel.dados_leito["bomba_infusao"]["ligado"],
            "temperatura": painel.dados_leito["sinais_vitais"]["temperatura"],
            "spo2": painel.dados_leito["sinais_vitais"]["spo2"],
            "freq_cardiaca": painel.dados_leito["sinais_vitais"]["freq_cardiaca"],
            "freq_respiratoria": painel.dados_leito["sinais_vitais"]["freq_respiratoria"],
            "pressao_arterial": painel.dados_leito["sinais_vitais"]["pressao_arterial"],
            "alertas": painel.dados_leito["sinais_vitais"]["alertas"],
            "irpm": painel.dados_leito["respirador"]["irpm"],
            "volume_corrente": painel.dados_leito["respirador"]["volume_corrente"],
            "respirador_ligado": painel.dados_leito["respirador"]["ligado"],
            "marca_passo": painel.dados_leito["cardioversor"]["identificador_marca_passo"],
            "potencia": painel.dados_leito["cardioversor"]["potencia"],
            "frequencia": painel.dados_leito["cardioversor"]["frequencia"],
            "cardioversor_ligado": painel.dados_leito["cardioversor"]["ligado"],
            "botao_ligado": painel.dados_leito["botao_emergencia"]["ligado"]}

context = update_context()


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Metodo para roteamento inicial do componente"""
    global context
    context = update_context()
    context["request"] = request
    update_painel()
    return templates.TemplateResponse("index.html",
                                      context)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/sinais", response_class=HTMLResponse)
async def sinais(request: Request):
    context = update_context()
    context["request"] = request
    update_painel()
    return templates.TemplateResponse("sinais_vitais.html",
                                      context)


@app.get("/bomba", response_class=HTMLResponse)
async def bomba(request: Request):
    context = update_context()
    context["request"] = request
    update_painel()
    return templates.TemplateResponse("bomba_infusao.html",
                                      context)


@app.get("/ligar_bomba")
def ligar_bomba_infusao():
    requests.put(f'{environment_vars["bomba_infusao_container_protocol"]}'
                 f'://{environment_vars["bomba_infusao_container_name"]}'
                 f':{environment_vars["bomba_infusao_container_port"]}'
                 f'/ligar',
                 timeout=5)
    print("Ligando Bomba")
    painel.dados_leito["bomba_infusao"]["ligado"] = True
    global context
    context = update_context()


@app.get("/desligar_bomba")
def desligar_bomba_infusao():
    requests.put(f'{environment_vars["bomba_infusao_container_protocol"]}'
                 f'://{environment_vars["bomba_infusao_container_name"]}'
                 f':{environment_vars["bomba_infusao_container_port"]}'
                 f'/desligar',
                 timeout=5)
    print("Desligando Bomba")
    painel.dados_leito["bomba_infusao"]["ligado"] = False
    global context
    context = update_context()


@app.get("/respirador", response_class=HTMLResponse)
async def respirador(request: Request):
    context = update_context()
    context["request"] = request
    update_painel()
    return templates.TemplateResponse("respirador.html",
                                      context)


@app.get("/ligar_respirador")
def ligar_respirador():
    requests.put(f'{environment_vars["respirador_container_protocol"]}'
                 f'://{environment_vars["respirador_container_name"]}'
                 f':{environment_vars["respirador_container_port"]}'
                 f'/ligar',
                 timeout=5)
    print("Ligando Respirador")
    painel.dados_leito["respirador"]["ligado"] = True
    global context
    context = update_context()


@app.get("/desligar_respirador")
def desligar_respirador():
    requests.put(f'{environment_vars["respirador_container_protocol"]}'
                 f'://{environment_vars["respirador_container_name"]}'
                 f':{environment_vars["respirador_container_port"]}'
                 f'/desligar',
                 timeout=5)
    print("Desligando Respirador")
    painel.dados_leito["respirador"]["ligado"] = False
    global context
    context = update_context()


@app.get("/cardioversor", response_class=HTMLResponse)
async def cardioversor(request: Request):
    context = update_context()
    context["request"] = request
    update_painel()
    return templates.TemplateResponse("cardioversor.html",
                                      context)


@app.get("/ligar_cardioversor")
def ligar_cardioversor():
    requests.put(f'{environment_vars["cardioversor_container_protocol"]}'
                 f'://{environment_vars["cardioversor_container_name"]}'
                 f':{environment_vars["cardioversor_container_port"]}'
                 f'/ligar',
                 timeout=5)
    print("Ligando Cardioversor")
    painel.dados_leito["cardioversor"]["ligado"] = True
    global context
    context = update_context()


@app.get("/desligar_cardioversor")
def desligar_cardioversor():
    requests.put(f'{environment_vars["cardioversor_container_protocol"]}'
                 f'://{environment_vars["cardioversor_container_name"]}'
                 f':{environment_vars["cardioversor_container_port"]}'
                 f'/desligar',
                 timeout=5)
    print("Desligando Cardioversor")
    painel.dados_leito["cardioversor"]["ligado"] = False
    global context
    context = update_context()


@app.get("/botao", response_class=HTMLResponse)
async def botao(request: Request):
    context = update_context()
    context["request"] = request
    update_painel()
    return templates.TemplateResponse("botao.html",
                                      context)


@app.get("/acionar_botao")
def acionar_botao():
    requests.put(f'{environment_vars["botao_emergencia_container_protocol"]}'
                 f'://{environment_vars["botao_emergencia_container_name"]}'
                 f':{environment_vars["botao_emergencia_container_port"]}'
                 f'/ligar',
                 timeout=5)
    print("Acionando Botão")
    painel.dados_leito["botao_emergencia"]["ligado"] = True
    global context
    context = update_context()


@app.get("/desligar_botao")
def desligar_botao():
    requests.put(f'{environment_vars["botao_emergencia_container_protocol"]}'
                 f'://{environment_vars["botao_emergencia_container_name"]}'
                 f':{environment_vars["botao_emergencia_container_port"]}'
                 f'/desligar',
                 timeout=5)
    print("Desligando Botão")
    painel.dados_leito["botao_emergencia"]["ligado"] = False
    global context
    context = update_context()

alerts = painel.dados_leito["sinais_vitais"]["alertas"]

if "spo2_baixa" in alerts or "freq_respiratoria_baixa" in alerts:
    ligar_respirador()
    
if "freq_cardiaca_baixa" in alerts or "freq_cardiaca_alta" in alerts:
    ligar_cardioversor()
    
if int(painel.dados_leito["sinais_vitais"]["spo2"]) < int(93):
    ligar_respirador()
    
