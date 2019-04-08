################################################################ Localhost Server ##################################################################

/* Drops all users if they already exist for the pc_screener database */

DROP USER IF EXISTS 'mlukina'@'localhost';

/* Creates users if they don't already exist for the pc_screener database */

CREATE USER IF NOT EXISTS 'mlukina'@'localhost' IDENTIFIED BY 'test1234';
GRANT ALL PRIVILEGES ON pc_screener_4.* TO 'mlukina'@'localhost' WITH GRANT OPTION;

/* Shows all current users */
SELECT user, host
FROM mysql.user;

########################################################### Conestoga Hub Ubuntu Server ############################################################

-- to drop:
DROP USER 'mlukina'@'localhost';

CREATE USER 'mlukina'@'localhost' IDENTIFIED BY 'test1234';
GRANT ALL PRIVILEGES ON pc_screener_4.* TO 'mlukina'@'localhost' WITH GRANT OPTION;

/* Shows all current users */
SELECT user, host, password
FROM mysql.user;