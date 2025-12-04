-- This script lists the number of records for each score in second_table
-- It prints: score and the count of records labeled as number
-- Results are sorted by number in descending order

SELECT scor, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
