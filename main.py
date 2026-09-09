from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Site Oficial - Mia Salvani", version="1.0.0")

BASE_DIR = Path(__file__).resolve().parent

app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

class Livro(BaseModel):
    id: int
    titulo: str
    ordem: str
    premissa: str
    capa_url: str

# Dados oficiais extraídos da série Cisnes de New York
CATALOGO_LIVROS = [
    {
        "id": 1,
        "titulo": "Albatroz",
        "ordem": "Cisnes de New York — Livro 1",
        "premissa": "O início do dark romance que introduz o universo intenso e sufocante dos Cisnes de New York.",
        "capa_url": "/static/images/capas/albatroz.jpg"
    },
    {
        "id": 2,
        "titulo": "Abutre",
        "ordem": "Cisnes de New York — Livro 2",
        "premissa": "Segunda parte da saga, aprofundando os segredos e as dinâmicas sombrias da autora.",
        "capa_url": "/static/images/capas/abutre.jpg"
    },
    {
        "id": 3,
        "titulo": "Harpia",
        "ordem": "Cisnes de New York — Livro 3",
        "premissa": "Dando continuidade à tensão implacável da série de dark romance de maior sucesso.",
        "capa_url": "/static/images/capas/harpia.jpg"
    },
    {
        "id": 4,
        "titulo": "Juízes",
        "ordem": "Prequel / Obra da Série",
        "premissa": "A obra que expande as origens e os dilemas que moldaram o universo dos Cisnes de New York.",
        "capa_url": "/static/images/capas/juizes.jpg"
    }
]

@app.get("/api/livros", response_model=List[Livro])
def listar_livros():
    return CATALOGO_LIVROS

@app.get("/")
def home_page(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")