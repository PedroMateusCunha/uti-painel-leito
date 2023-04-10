from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/bomba", response_class=HTMLResponse)
async def home(request: Request):
    # Obtém o status da Bomba de Infusão
    response = requests.get("http://10.0.0.254:7002/status")
    data = response.json()

    # Renderiza o template HTML com os dados do status da Bomba de Infusão
    return templates.TemplateResponse("bomba_infusao.html",
                                      {"request": request,
                                        "taxa_med1": data['taxas']['med1'],
                                        "taxa_med2": data['taxas']['med2'],
                                        "taxa_soro": data['taxas']['soro'],
                                        "qtd_med1": data['quantidades']['med1'],
                                        "qtd_med2": data['quantidades']['med2'],
                                        "qtd_soro": data['quantidades']['soro']})

@app.get("/sinais", response_class=HTMLResponse)
async def home(request: Request):
    # Obtém o status da Bomba de Infusão
    response = requests.get("http://10.0.0.254:7001/sinais_vitais")
    data = response.json()
    sinais_vitais = data['sinais_vitais']
    alertas = data['alertas']

    # Renderiza o template HTML com os dados do status da Bomba de Infusão
    return templates.TemplateResponse("sinais_vitais.html",
                                      {"request": request,
                                        "temperatura": sinais_vitais['temperatura'],
                                        "spo2": sinais_vitais['spo2'],
                                        "freq_cardiaca": sinais_vitais['freq_cardiaca'],
                                        "freq_respiratoria": sinais_vitais['freq_respiratoria'],
                                        "pressao_arterial": sinais_vitais['pressao_arterial'],
                                        "alertas": alertas})

@app.get("/cardioversor", response_class=HTMLResponse)
async def home(request: Request):
    # Obtém o status da Bomba de Infusão
    response = requests.get("http://10.0.0.254:7004/status")
    data = response.json()
    if data['ligado'] == True:
        ligado = "Ligado"
    else:
        ligado = "Desligado"
    # Renderiza o template HTML com os dados do status da Bomba de Infusão
    return templates.TemplateResponse("cardioversor.html",
                                      {"request": request,
                                        "marca_passo": data['identificador_marca_passo'],
                                        "potencia": data['potencia'],
                                        "frequencia": data['frequencia'],
                                        "ligado": ligado}) 

# @app.get("/", response_class=HTMLResponse)
# async def home(request: Request):
#     # Renderiza o template HTML do painel de leito
#     return templates.TemplateResponse("painel.html", {"request": request})

@app.get('/bomba/status')
async def bomba_status():
    # Obtem o status da Bomba de Infusão
    response = requests.get("http://10.0.0.254:7002/status")
    data = response.json()
    html_content = templates.render(status=data['status'], atualizacao=data['atualizacao'])
    return html_content

@app.put('/bomba/medicamento/{medicamento}/{quantidade}')
async def bomba_set_quantidade(medicamento: str, quantidade: int):
    # Define a quantidade de medicamentos na Bomba de Infusão
    response = requests.put(f'http://localhost:8000/medicamento/{medicamento}/{quantidade}')
    return response.json()

@app.put('/bomba/taxa/{medicamento}/{taxa}')
async def bomba_set_taxa(medicamento: str, taxa: int):
    # Define a taxa de infusão dos medicamentos na Bomba de Infusão
    response = requests.put(f'http://localhost:8000/taxa/{medicamento}/{taxa}')
    return response.json()

@app.put('/bomba/ligar')
async def bomba_ligar():
    # Liga a Bomba de Infusão
    response = requests.put('http://localhost:8000/ligar')
    return response.json()

@app.put('/bomba/desligar')
async def bomba_desligar():
    # Desliga a Bomba de Infusão
    response = requests.put('http://localhost:8000/desligar')
    return response.json()

@app.get('/respirador/status')
async def respirador_status():
    # Obtem o status do Respirador
    response = requests.get('http://localhost:8001/status')
    return response.json()

@app.put('/respirador/irpm/{irpm}')
async def respirador_set_irpm(irpm: int):
    # Define o valor de IRPM do Respirador
    response = requests.put(f'http://localhost:8001/irpm/{irpm}')
    return response.json()

@app.put('/respirador/vc/{vc}')
async def respirador_set_vc(vc: int):
    # Define o valor de VC do Respirador
    response = requests.put(f'http://localhost:8001/vc/{vc}')
    return response.json()

@app.put('/respirador/ligar')
async def respirador_ligar():
    # Liga o Respirador
    response = requests.put('http://localhost:8001/ligar')
    return response.json()

@app.put('/respirador/desligar')
async def respirador_desligar():
    # Desliga o Respirador
    response = requests.put('http://localhost:8001/desligar')
    return response.json()