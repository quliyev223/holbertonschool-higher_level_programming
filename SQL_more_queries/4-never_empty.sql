-- Requirements:
-- 1. Create the table 'id_not_null' in the database passed as an argument to the mysql command.
-- 2. The table should have the following columns:
--    - id INT with DEFAULT value 1
--    - name VARCHAR(256)
-- 3. If the table 'id_not_null' already exists, the script should not fail.

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);

