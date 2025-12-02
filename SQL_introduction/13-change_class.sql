-- 13-change_class.sql
-- Deletes every record in second_table where the score is 5 or lower
-- Only uses the score field (no id, no name needed)

DELETE FROM second_table WHERE score <= 5;
