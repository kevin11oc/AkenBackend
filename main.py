from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:4200",
    "http://127.0.0.1:4200",
    "https://tu-dominio.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/scrapy")
def scrape():
    url = "https://www.infobae.com/colombia/2025/02/26/apuestas-en-linea-en-jaque-aplicar-iva-a-estas-plataformas-podria-impulsar-mercado-negro-y-afectar-el-recaudo-fiscal-en-colombia/"
    
    response = requests.get(url)
    
    if response.status_code != 200:
        return {"error": "No se pudo acceder a la página"}
    
    soup = BeautifulSoup(response.text, "html.parser")
    titulo = soup.find("h1")
    titulo_texto = titulo.text.strip() if titulo else "No se encontró el título"
    autor = soup.find("a", class_="author-name")
    autor_texto = autor.text.strip() if autor else "No encontrado"
    hora = soup.find("span", class_="sharebar-article-date")
    hora_texto = hora.text.strip() if hora else "No encontrado"
    resumen = soup.find("h2", class_ = "article-subheadline")
    resumen_texto = resumen.text.strip() if resumen else "No encontrado"

    return {"titulo": titulo_texto, "autor": autor_texto, "hora": hora_texto, "resumen": resumen_texto}

