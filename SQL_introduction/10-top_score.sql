-- 10-top_score.sql
-- Lists all rows from second_table
-- Shows score first, then name
-- Ordered by score descending (highest score on top)

SELECT score, name
FROM second_table
ORDER BY score DESC;
