-- Script creates table id_not_null
-- The database name will be passed as an argument of the mysql
-- If the table id_not_null already exists, does not fail
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
