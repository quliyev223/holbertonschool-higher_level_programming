-- 12-no_cheating.sql
-- Updates the score of Bob to 10 using only the name field
-- We are not allowed to use the id value at all

UPDATE second_table
SET score = 10
WHERE name = 'Bob';
