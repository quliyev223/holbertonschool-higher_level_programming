-- This script lists all records from second_table except those where name is empty or NULL
-- It must output only score and name, in that order
-- Results must be sorted by score in descending order

-- Do not list rows where name has no value (empty string or NULL)
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name <> ''

-- Sort results by score from highest to lowest
ORDER BY score DESC;
