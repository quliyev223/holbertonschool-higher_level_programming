-- Script to create the database hbtn_0d_usa and the table cities
-- Database: hbtn_0d_usa
-- If the database already exists, this script will not fail
-- Table: cities
-- If the table already exists, this script will not fail
-- id is an INT that is unique, auto-incremented, not null, and the primary key
-- state_id is an INT that cannot be null and is a FOREIGN KEY referencing states.id
-- name is a VARCHAR(256) that cannot be null

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
CONSTRAINT fk_state FOREIGN KEY (state_id) REFERENCES states(id)
);

