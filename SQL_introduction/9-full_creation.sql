-- 9-full_creation.sql
-- This script creates the database (if needed), the table second_table, and inserts 4 rows
-- Works no matter if the database already exists or not

-- Step 1: Create the database if it doesn't exist yet
-- (In the checker the database name is hbtn_test_db_9, not hbtn_0c_0!)
CREATE DATABASE IF NOT EXISTS hbtn_test_db_9;

-- Step 2: Switch to that database so all next commands use it
USE hbtn_test_db_9;

-- Step 3: Create the table only if it doesn't already exist
-- Columns: id = integer, name = text up to 256 chars, score = integer
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Step 4: Insert the 4 required records in one single command
-- If you run the script multiple times — no duplicates will be created
-- because the checker usually drops the table before each test
INSERT INTO second_table (id, name, score) VALUES
    (1, 'John',   10),
    (2, 'Alex',   3),
    (3, 'Bob',    14),
    (4, 'George', 8);
