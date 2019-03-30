DROP DATABASE IF EXISTS pc_screener; 

CREATE DATABASE IF NOT EXISTS pc_screener;

USE pc_screener;

CREATE TABLE IF NOT EXISTS users (
	id				INT				NOT NULL		AUTO_INCREMENT		PRIMARY KEY, 
    username		VARCHAR(32)		NOT NULL,
    password		VARCHAR(32)		NOT NULL,
    email			VARCHAR(64)		NOT NULL
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS sex (
    id				TINYINT					NOT NULL		AUTO_INCREMENT		PRIMARY KEY,
    sex				VARCHAR(16)				NOT NULL
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS primary_language (
    primary_language_code	CHAR(3)				NOT NULL		PRIMARY KEY,
    primary_language		VARCHAR(7)			NOT NULL
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS self_reported_health (
	id									TINYINT				NOT NULL		AUTO_INCREMENT		PRIMARY KEY,
    self_reported_health_value			TINYINT				NOT NULL,
    self_reported_health_description	VARCHAR(32)			NOT NULL
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS patient (
	id 						INT 			  	NOT NULL 	  	AUTO_INCREMENT		PRIMARY KEY,
    first_name 	  			VARCHAR(32)		  	NOT NULL,
    last_name	    		VARCHAR(32)		  	NOT NULL,
    sex_id					TINYINT				NOT NULL,
    primary_language_code	CHAR(3)				NOT NULL, 
    time_recorded 			TIMESTAMP	  	  	DEFAULT 		CURRENT_TIMESTAMP,
	FOREIGN KEY fk_primary_language (primary_language_code)
		REFERENCES primary_language (primary_language_code),
    FOREIGN KEY fk_sex (sex_id)
		REFERENCES sex(id)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS screener_instance (
	id 						INT 			  	NOT NULL 	  	AUTO_INCREMENT		PRIMARY KEY,
    patient_id				INT					NOT NULL,
    self_reported_health 	SMALLINT		  	NOT NULL,
	FOREIGN KEY fk_patient_id (patient_id)
	REFERENCES patient(id)
) ENGINE = InnoDB;

INSERT INTO users (id, username, password, email) VALUES
(default, "Mlukina", "test1234", "mikelukina@gmail.com"),
(default, "HShoukat", "test5678", "test@gmail.com"),
(default, "PMadziak", "conestogahi", "PMadziak@gmail.com"); 

INSERT INTO primary_language (primary_language_code, primary_language) VALUES
("eng", "English"),
("fre", "French");

INSERT INTO sex (id, sex) VALUES
(default, "Male"),
(default, "Female");

INSERT INTO self_reported_health (id, self_reported_health_value, self_reported_health_description) VALUES
(default, 0, "Excellent"),
(default, 1, "Good"),
(default, 2, "Fair"),
(default, 3, "Poor"),
(default, 8, "Could not (would not) respond");

INSERT INTO patient (id, first_name, last_name, sex_id, primary_language_code, time_recorded) VALUES
(default, "Mike", "Lukina", 1, "eng", default),
(default, "Hamza", "Shoukat", 2, "fre", default);

INSERT INTO screener_instance (id, patient_id, self_reported_health) VALUES
(default, 2, 0)