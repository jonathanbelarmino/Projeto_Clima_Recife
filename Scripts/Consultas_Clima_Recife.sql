CREATE TABLE clima_recife (
    id SERIAL PRIMARY KEY,
    cidade VARCHAR(50),
    data_coleta TIMESTAMP,
    temperatura NUMERIC,
    sensacao_termica NUMERIC,
    umidade INT,
    pressao INT,
    velocidade_vento NUMERIC,
    descricao VARCHAR(100)
);

-- Média de temperatura
SELECT AVG(temperatura) FROM clima_recife;

-- Temperatura máxima e mínima
SELECT MAX(temperatura), MIN(temperatura) FROM clima_recife;

-- Clima mais frequente
SELECT descricao, COUNT(*) 
FROM clima_recife
GROUP BY descricao
ORDER BY COUNT(*) DESC;