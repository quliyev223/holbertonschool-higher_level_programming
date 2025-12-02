-- 4-first_table.sql
-- This script creates a table called 'first_table' in the current database
-- The database name is passed as an argument when calling mysql (e.g. "mysql db_name")

-- We use CREATE TABLE IF NOT EXISTS so the script doesn't fail
-- if the table was already created before (very important requirement!)
CREATE TABLE IF NOT EXISTS first_table (
    -- Column 'id' - integer type
    id INT,
    
    -- Column 'name' - text up to 256 characters
    name VARCHAR(256)
);

-- That's all! No SELECT or SHOW allowed - only CREATE TABLE
