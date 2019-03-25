DROP DATABASE IF EXISTS pc_screener; 

CREATE DATABASE IF NOT EXISTS pc_screener;

USE pc_screener;

CREATE TABLE IF NOT EXISTS primary_language (
	id						SMALLINT			NOT NULL		AUTO_INCREMENT		PRIMARY KEY,
    primary_language_code	CHAR(3)				NOT NULL,
    primary_language		VARCHAR(7)			NOT NULL
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS self_reported_health (
	id									SMALLINT			NOT NULL		AUTO_INCREMENT		PRIMARY KEY,
    self_reported_health_value			CHAR(3)				NOT NULL,
    self_reported_health_description	VARCHAR(32)			NOT NULL
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS patient (
	id 					INT 			  	NOT NULL 	  	AUTO_INCREMENT		PRIMARY KEY,
    first_name 	  		VARCHAR(32)		  	NOT NULL,
    last_name	    	VARCHAR(32)		  	NOT NULL,
    primary_language_id	SMALLINT			NOT NULL, 
    time_recorded 		TIMESTAMP	  	  	DEFAULT 		CURRENT_TIMESTAMP,
	FOREIGN KEY fk_primary_language (primary_language_id)
	REFERENCES primary_language(id)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS screener_instance (
	id 						INT 			  	NOT NULL 	  	AUTO_INCREMENT		PRIMARY KEY,
    patient_id				INT					NOT NULL,
    self_reported_health 	SMALLINT		  	NOT NULL,
	FOREIGN KEY fk_patient_id (patient_id)
	REFERENCES patient(id)
) ENGINE = InnoDB;

INSERT INTO primary_language (id, primary_language_code, primary_language) VALUES
(default, "eng", "English"),
(default, "fre", "French");

INSERT INTO self_reported_health (id, self_reported_health_value, self_reported_health_description) VALUES
(default, "0", "Excellent"),
(default, "1", "Good"),
(default, "2", "Fair"),
(default, "3", "Poor"),
(default, "8", "Could not (would not) respond");

INSERT INTO patient (id, first_name, last_name, primary_language_id, time_recorded) VALUES
(default, "Mike", "Lukina", 1, default),
(default, "Hamza", "Shoukat", 2, default);

INSERT INTO screener_instance (id, patient_id, self_reported_health) VALUES
(default, 2, 0)