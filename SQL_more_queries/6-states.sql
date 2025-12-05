-- Script to create the database hbtn_0d_usa and the table states
-- Database: hbtn_0d_usa
-- If the database already exists, the script will not fail
-- Table: states
-- If the table already exists, the script will not fail
-- id is an INT that is unique, auto-incremented, not null, and the primary key
-- name is a VARCHAR(256) that cannot be null

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(256) NOT NULL
);
