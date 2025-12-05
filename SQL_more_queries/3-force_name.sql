-- Holberton SQL_more_queries - Task 3: Create table force_name
--
-- Requirements:
-- 1. Create the table 'force_name' in the database passed as an argument to the mysql command.
-- 2. The table should have the following columns:
--    - id INT
--    - name VARCHAR(256) NOT NULL
-- 3. If the table 'force_name' already exists, the script should not fail.

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
