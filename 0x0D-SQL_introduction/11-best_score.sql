-- Lists all records with a score >= 10 in the table second_table
-- The database name will be passed as an argument of the mysql
SELECT score, name
       WHERE score >= 10
       ORDER BY score DESC;
