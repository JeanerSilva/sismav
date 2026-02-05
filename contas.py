import pandas as pd
import random
import os

# -----------------------------------
# CONFIGURAÇÕES
# -----------------------------------
NUM_EMPRESAS = 50   # ajuste se quiser mais
CONTAS = [
    "1844500002","1844510009","1844515004","1844520006",
    "1989045006","3044500006","3044600009","3044610006",
    "3044615001","3044620003","3044700002","3044710009",
    "3044720006","3046020003"
]

# Faixas de valores por porte
FAIXAS = {
    "grande": (500000, 5000000),
    "media":  (50000, 500000),
    "pequena": (1000, 50000)
}

# Data fixa
DATABASE = "07/02/2026"
DATABASE_FILENAME = DATABASE.replace("/", "-")  # vira 04-02-2026

# -----------------------------------
# FUNÇÕES AUXILIARES
# -----------------------------------
def classificar_porte():
    r = random.random()
    if r < 0.2:
        return "grande"
    elif r < 0.7:
        return "media"
    else:
        return "pequena"

# -----------------------------------
# GERAR EMPRESAS COM NOMES PADRONIZADOS
# -----------------------------------
empresas = [(f"CNPJ{i+1}___", classificar_porte()) for i in range(NUM_EMPRESAS)]

# -----------------------------------
# GERAR LINHAS DE CONTAS
# -----------------------------------
linhas = []

for cnpj, porte in empresas:
    minimo, maximo = FAIXAS[porte]
    for conta in CONTAS:
        saldo = round(random.uniform(minimo, maximo), 2)
        linhas.append([
            cnpj,
            conta,
            str(saldo).replace('.', ','),
            DATABASE  # nova coluna fixa
        ])

df = pd.DataFrame(linhas, columns=[
    "empresaCNPJ",
    "codigoConta",
    "saldoDia",
    "dataBase"
])

# -----------------------------------
# CRIAR PASTA /contas SE NÃO EXISTIR
# -----------------------------------
os.makedirs("contas", exist_ok=True)

# -----------------------------------
# SALVAR ARQUIVO COM NOME BASEADO NA DATA
# -----------------------------------
caminho_arquivo = f"contas/{DATABASE_FILENAME}-contas.csv"
df.to_csv(caminho_arquivo, sep=";", index=False, encoding="utf-8")

print(f"Arquivo gerado com sucesso em: {caminho_arquivo}")