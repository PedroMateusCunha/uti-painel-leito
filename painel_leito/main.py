from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/sinais", response_class=HTMLResponse)
async def sinais(request: Request):
    # Obtém o status da Bomba de Infusão
    response = requests.get("http://10.0.0.254:7001/status")
    data = response.json()["sinais_vitais"]

    # Renderiza o template HTML com os dados do status da Bomba de Infusão
    return templates.TemplateResponse("sinais_vitais.html",
                                      {"request": request,
                                        "temperatura": data["temperatura"],
                                        "spo2": data["spo2"],
                                        "freq_cardiaca": data["freq_cardiaca"],
                                        "freq_respiratoria": data["freq_respiratoria"],
                                        "pressao_arterial": data["pressao_arterial"],
                                        "alertas": data["alertas"]})

@app.get("/bomba", response_class=HTMLResponse)
async def bomba(request: Request):
    # Obtém o status da Bomba de Infusão
    response = requests.get("http://10.0.0.254:7002/status")
    data = response.json()["bomba_infusao"]

    # Renderiza o template HTML com os dados do status da Bomba de Infusão
    return templates.TemplateResponse("bomba_infusao.html",
                                      {"request": request,
                                        "taxa_med1": data['taxas']['med1'],
                                        "taxa_med2": data['taxas']['med2'],
                                        "taxa_soro": data['taxas']['soro'],
                                        "qtd_med1": data['quantidades']['med1'],
                                        "qtd_med2": data['quantidades']['med2'],
                                        "qtd_soro": data['quantidades']['soro']})


@app.get("/cardioversor", response_class=HTMLResponse)
async def cardioversord(request: Request):
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
