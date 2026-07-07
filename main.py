from fastapi import FastAPI, Query
import requests
from models import Produto
import models

app = FastAPI()

@app.get("/produtos")
def listar_produtos():
    estoque = models.carregar_produtos()
    return estoque 

@app.post("/produtos")
def criar_produtos(produto: Produto):   
    estoque = models.carregar_produtos()
    estoque.append(produto.model_dump())
    models.salvar_produtos(estoque)
    return produto