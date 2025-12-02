-- Task: Print the full description of the table 'first_table'
-- from the database passed as argument to the mysql command
-- IMPORTANT: We are NOT allowed to use DESCRIBE or EXPLAIN

-- SHOW CREATE TABLE does exactly what we need:
-- it returns the complete CREATE TABLE statement that was used
-- to create the table, including columns, types, defaults, engine, charset, etc.
-- This is the only allowed way to get the full table description without DESCRIBE/EXPLAIN

SHOW CREATE TABLE first_table;
