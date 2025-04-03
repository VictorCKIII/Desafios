SELECT 
    o.razao_social,
    o.nome_fantasia,
    SUM(CAST(REPLACE(t.vl_final, ',', '.') AS NUMERIC)) AS total_despesas_anual
FROM (
    -- Primeiro Trimestre 2024
    SELECT reg_ans, vl_final 
    FROM PrimeiroT2024
    WHERE description ILIKE '%EVENTOS%SINISTROS%ASSISTÊNCIA%SAÚDE%MEDICO HOSPITALAR%'
    
    UNION ALL
    
    -- Segundo Trimestre 2024
    SELECT reg_ans, vl_final 
    FROM SegundoT2024
    WHERE description ILIKE '%EVENTOS%SINISTROS%ASSISTÊNCIA%SAÚDE%MEDICO HOSPITALAR%'
    
    UNION ALL
    
    -- Terceiro Trimestre 2024
    SELECT reg_ans, vl_final 
    FROM TerceiroT2024
    WHERE description ILIKE '%EVENTOS%SINISTROS%ASSISTÊNCIA%SAÚDE%MEDICO HOSPITALAR%'
    
    UNION ALL
    
    -- Quarto Trimestre 2024
    SELECT reg_ans, vl_final 
    FROM QuartoT2024
    WHERE description ILIKE '%EVENTOS%SINISTROS%ASSISTÊNCIA%SAÚDE%MEDICO HOSPITALAR%'
) t
JOIN 
    Operadoras o ON t.reg_ans = o.registro_ans
GROUP BY 
    o.razao_social, o.nome_fantasia
ORDER BY 
    total_despesas_anual DESC
LIMIT 10;