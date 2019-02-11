/* Drops all users if they already exist for the pc_screener database */

DROP USER IF EXISTS 'Mlukina'@'localhost', 'Hshoukat'@'localhost', 'Pmadziak'@'localhost';

/* Creates users if they don't already exist for the pc_screener database */

CREATE USER IF NOT EXISTS 'Mlukina'@'localhost' IDENTIFIED BY 'test1';
GRANT ALL PRIVILEGES ON pc_screener.* TO 'Mlukina'@'localhost' WITH GRANT OPTION;

CREATE USER IF NOT EXISTS 'Hshoukat'@'localhost' IDENTIFIED BY 'test2';
GRANT ALL PRIVILEGES ON pc_screener.* TO 'Hshoukat'@'localhost' WITH GRANT OPTION;

CREATE USER IF NOT EXISTS 'Pmadziak'@'localhost' IDENTIFIED BY 'test3';
GRANT ALL PRIVILEGES ON pc_screener.* TO 'Pmadziak'@'localhost' WITH GRANT OPTION;

/* Shows all current users */
SELECT user, host
FROM mysql.user;