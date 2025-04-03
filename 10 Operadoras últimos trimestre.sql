SELECT 
    o.razao_social, 
    o.nome_fantasia,
    SUM(CAST(REPLACE(q.vl_final, ',', '.') AS NUMERIC)) AS total_despesas
FROM 
    QuartoT2024 q
JOIN 
    Operadoras o ON q.reg_ans = o.registro_ans
WHERE 
    q.description ILIKE '%EVENTOS%SINISTROS%ASSISTÊNCIA%SAÚDE%MEDICO HOSPITALAR%'
GROUP BY 
    o.razao_social, o.nome_fantasia
ORDER BY 
    total_despesas DESC
LIMIT 10;