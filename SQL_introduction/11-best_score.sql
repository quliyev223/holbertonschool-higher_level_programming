-- 11-best_score.sql
-- Lists all records from second_table where score >= 10
-- Displays score first, then name
-- Ordered by score descending (highest score on top)

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
