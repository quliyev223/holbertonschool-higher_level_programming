-- Holberton SQL_more_queries - Task 1: Create user
-- 
-- Requirements:
-- 1. Create the MySQL server user 'user_0d_1'.
-- 2. The password for 'user_0d_1' should be 'user_0d_1_pwd'.
-- 3. The user should have all privileges on your MySQL server (*.*).
-- 4. If the user already exists, the script should not fail.

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
