-- 8-count_89.sql
-- This script shows how many records in 'first_table' have id = 89
-- It outputs ONLY the number (nothing else), exactly as required

-- We use SELECT COUNT(*) to count rows
-- WHERE id = 89 filters only the rows with that id
-- This query returns a single column with a single row: the count

SELECT COUNT(*) FROM first_table WHERE id = 89;

-- Important notes (for beginners):
-- - COUNT(*) counts ALL matching rows
-- - No extra text, no column name like "count" will appear because MySQL shows just the number when you run via pipe
-- - Running this after inserting the row 3 times with the previous script will show: 3
