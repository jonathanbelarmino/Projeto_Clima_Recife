📊 Projeto: Análise Climática de Recife - Tendências e Impactos

📌 Descrição

Este projeto tem como objetivo coletar, armazenar e analisar dados climáticos da cidade de Recife - PE, utilizando uma pipeline de dados completa que envolve extração via API, armazenamento em banco de dados e visualização em dashboard interativo.

A análise busca identificar padrões climáticos, variações de temperatura e comportamento da umidade ao longo do tempo.

🚀 Tecnologias Utilizadas

Python
API (OpenWeather)
PostgreSQL
Power BI
SQL

🧠 Arquitetura do Projeto

API (OpenWeather)
        ↓
Python (Coleta e Tratamento)
        ↓
PostgreSQL (Armazenamento)
        ↓
Power BI (Visualização e Análise)

🔄 Pipeline de Dados (ETL)

1. Extração

Dados coletados via API OpenWeather
Informações como temperatura, umidade, vento e descrição climática

2. Transformação

Tratamento de dados no Python
Padronização de campos
Criação de variáveis derivadas (ex: classificação de temperatura)

3. Carga

Armazenamento no PostgreSQL
Estrutura tabular para análise histórica

📊 Modelagem de Dados

Tabela principal: clima_recife

Campos:

cidade
data_coleta
temperatura
sensacao_termica
umidade
pressao
velocidade_vento
descricao

📈 Dashboard

O dashboard foi desenvolvido no Power BI com foco em análise exploratória e geração de insights.

Principais indicadores:

Média de temperatura
Temperatura máxima e mínima
Média de umidade
Tendência de temperatura

Principais análises:

Variação da temperatura ao longo do tempo
Variação da umidade
Clima mais frequente
Intensidade dos ventos

🔍 Insights Obtidos

A temperatura média manteve-se entre 26°C e 30°C, indicando baixa variação térmica ao longo do período analisado
Predominância de dias com “few clouds”, indicando baixa incidência de chuvas
A umidade permaneceu elevada durante todo o período, característica do clima tropical da região
Tendência de leve aumento na temperatura ao longo do período

⚙️ Como Executar o Projeto

Clonar o repositório:

"git clone https://github.com/seu-usuario/seu-repositorio.git"

Instalar dependências:

"pip install requests psycopg2"

Configurar variáveis:
Inserir sua API Key do OpenWeather
Configurar conexão com PostgreSQL

Executar o script Python:

python coleta_clima.py

📌 Possíveis Melhorias

Automatização da coleta diária (scheduler)
Integração com dados históricos (INMET)
Criação de modelo dimensional (Data Warehouse)
Deploy do dashboard

👨‍💻 Autor

Jonathan Belarmino
Projeto desenvolvido para fins de estudo e portfólio na área de Análise de Dados.












