/* Drops all users if they already exist for the pc_screener database */

DROP USER IF EXISTS 'Mlukina'@'localhost';

/* Creates users if they don't already exist for the pc_screener database */

CREATE USER IF NOT EXISTS 'Mlukina'@'localhost' IDENTIFIED BY 'test1234';
GRANT ALL PRIVILEGES ON pc_screener.* TO 'Mlukina'@'localhost' WITH GRANT OPTION;

/* Shows all current users */
SELECT user, host
FROM mysql.user;