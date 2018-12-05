-- Creates the table unique_id
-- The database name will be passed as an argument of the mysql
-- If the table unique_id already exists,  script does not fail
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1, name VARCHAR(256), UNIQUE (id));
