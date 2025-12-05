-- Holberton SQL_more_queries - Task 2: Create database and read-only user
--
-- Requirements:
-- 1. Create the database 'hbtn_0d_2'.
-- 2. Create the MySQL server user 'user_0d_2'.
-- 3. The password for 'user_0d_2' should be 'user_0d_2_pwd'.
-- 4. Give 'user_0d_2' only SELECT privilege on the database 'hbtn_0d_2'.
-- 5. If the database 'hbtn_0d_2' already exists, the script should not fail.
-- 6. If the user 'user_0d_2' already exists, the script should not fail.

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
