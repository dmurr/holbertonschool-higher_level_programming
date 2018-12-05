-- Script creates a table called force_name
-- Database name will be passed
-- If it already exists, it will not fail
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
