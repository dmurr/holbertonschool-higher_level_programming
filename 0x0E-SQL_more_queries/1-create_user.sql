-- Creates the MySQL server user user_0d_1
-- Sets pass to user_0d_1_pwd and grants all privileges
-- Does not fail is user already exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
