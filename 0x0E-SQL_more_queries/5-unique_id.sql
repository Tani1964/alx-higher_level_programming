-- Script that creates the table unique_id on MySQL server.
-- unique_id description: id INT with the default value 1 and must be unique, and name VARCHAR(256).
CREATE TABLE IF NOT EXISTS unique_id (id INT NOT NULL DEFAULT 1 UNIQUE, name VARCHAR(256));
