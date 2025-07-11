-- SQLite
SELECT data, sum(quantidade_produzida)
FROM producao_producao
GROUP BY data;