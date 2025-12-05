-- Script to create the table unique_id
-- id is an INT with a default value of 1 and must be unique
-- name is a VARCHAR(256)
-- The database name will be passed as an argument of the mysql command
-- If the table unique_id already exists, this script will not fail

CREATE TABLE IF NOT EXISTS unique_id (
id INT DEFAULT 1 UNIQUE,
name VARCHAR(256)
);
