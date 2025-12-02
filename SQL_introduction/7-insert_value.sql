-- 7-insert_value.sql
-- This script inserts a new row into the table 'first_table' in the database hbtn_0c_0
-- The database name is passed as an argument when running the mysql command

-- We use the INSERT INTO statement to add a new record
-- We specify the exact columns (id and name) and their values
INSERT INTO first_table (id, name) VALUES (89, 'Best School');

-- That's it! 
-- Every time you run this script, it will add ONE new row with id=89 and name='Best School'
-- If you run it multiple times, you will get multiple identical rows (as shown in the example)
-- This is normal because there is no UNIQUE constraint on the 'id' column in this task
