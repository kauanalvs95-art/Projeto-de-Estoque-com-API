from pydantic import BaseModel
import os
import json


class Produto(BaseModel):
    sku: str
    nome: str
    quantidade: int
    preco: float
    localizacao: str
        
def carregar_produtos():
    try:
        with open("data/produtos.json", "r", encoding="utf-8") as arquivo:
            produtos = json.load(arquivo)
            return produtos
    except (FileNotFoundError, json.JSONDecodeError):
        return []
        
def salvar_produtos(produtos):
    os.makedirs("data", exist_ok=True)
    with open("data/produtos.json", "w", encoding="utf-8") as arquivo:
        json.dump(produtos, arquivo, indent=4)

def obter_produto_por_sku(sku: str):
    produtos = carregar_produtos()
    for produto in produtos:
        if produto["sku"] == sku:
            return produto
    return None