-- This script computes the average score from the table second_table
-- The resulting column must be named "average"
-- The database name is provided as an argument to the mysql command

SELECT AVG(score) AS average FROM second_table;
