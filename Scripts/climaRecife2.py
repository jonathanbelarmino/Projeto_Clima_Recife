import requests
import psycopg2
from datetime import datetime

# ======================
# 1️⃣ CONSUMIR API
# ======================

API_KEY = "eff1095f3d70655def86853cb38d1da6"
cidade_api = "Recife"

url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade_api}&appid={API_KEY}&units=metric"

response = requests.get(url)
dados = response.json()

cidade = dados["name"]
data_coleta = datetime.fromtimestamp(dados["dt"])
temperatura = dados["main"]["temp"]
sensacao_termica = dados["main"]["feels_like"]
umidade = dados["main"]["humidity"]
pressao = dados["main"]["pressure"]
velocidade_vento = dados["wind"]["speed"]
descricao = dados["weather"][0]["description"]

# ======================
# 2️⃣ CONECTAR NO BANCO
# ======================

conn = psycopg2.connect(
    host="localhost",
    database="projeto_clima",
    user="postgres",
    password="belarmino99"
)

cursor = conn.cursor()

# ======================
# 3️⃣ INSERIR DADOS
# ======================

sql = """
INSERT INTO clima_recife
(cidade, data_coleta, temperatura, sensacao_termica, umidade, pressao, velocidade_vento, descricao)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

valores = (
    cidade,
    data_coleta,
    temperatura,
    sensacao_termica,
    umidade,
    pressao,
    velocidade_vento,
    descricao
)

cursor.execute(sql, valores)
conn.commit()

print("✅ Dados inseridos com sucesso!")

cursor.close()
conn.close()