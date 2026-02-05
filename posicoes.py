import pandas as pd
import random
import os

# -----------------------------------
# CONFIGURAÇÕES
# -----------------------------------
NUM_LINHAS = 5000
NUM_EMPRESAS = 50
NUM_CLIENTES = 200   # ajuste conforme desejar
TICKERS = ["BTC", "ETH", "SOL", "USDT", "XRP", "ADA"]

# Data fixa
DATABASE = "08/02/2026"
DATABASE_FILENAME = DATABASE.replace("/", "-")  # vira 04-02-2026

# -----------------------------------
# GERAR LISTA DE CNPJs PADRONIZADOS
# -----------------------------------
CNPJS = [f"CNPJ{i+1}___" for i in range(NUM_EMPRESAS)]

# -----------------------------------
# GERAR LISTA DE CLIENTES FIXOS
# -----------------------------------
CLIENTES = [f"CLIENTE{i+1}" for i in range(NUM_CLIENTES)]

# -----------------------------------
# FUNÇÃO PARA GERAR UMA LINHA
# -----------------------------------
def gerar_linha():
    empresa = random.choice(CNPJS)
    cliente = random.choice(CLIENTES)
    tipo = random.choice([1, 2])
    ticker = random.choice(TICKERS)
    quantidade = round(random.uniform(0.01, 10), 8)
    valor = round(random.uniform(1000, 500000), 2)

    return [
        empresa,
        cliente,
        tipo,
        ticker,
        "tickerID_exemplo",
        "DLT_exemplo",
        "DLTID_exemplo",
        str(quantidade).replace('.', ','),
        str(valor).replace('.', ','),
        "Z1234567",
        "BR",
        DATABASE
    ]

# -----------------------------------
# GERAR AS 5000 LINHAS
# -----------------------------------
linhas = [gerar_linha() for _ in range(NUM_LINHAS)]

df = pd.DataFrame(linhas, columns=[
    "empresaCNPJ",
    "clienteId",
    "tipoCliente",
    "ticker",
    "tickerID",
    "DLT",
    "DLTID",
    "quantidade",
    "valor",
    "psavCustodiante",
    "psavCustodiantePais",
    "dataBase"
])

# -----------------------------------
# CRIAR PASTA /posicoes SE NÃO EXISTIR
# -----------------------------------
os.makedirs("posicoes", exist_ok=True)

# -----------------------------------
# SALVAR ARQUIVO COM NOME BASEADO NA DATA
# -----------------------------------
caminho_arquivo = f"posicoes/{DATABASE_FILENAME}-posicoes.csv"
df.to_csv(caminho_arquivo, sep=";", index=False, encoding="utf-8")

print(f"Arquivo gerado com sucesso em: {caminho_arquivo}")