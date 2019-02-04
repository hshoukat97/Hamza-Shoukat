CREATE DATABASE IF NOT EXISTS pc_screener;

USE pc_screener;

CREATE TABLE IF NOT EXISTS screener_instance (
	id 						INT 			  NOT NULL 	  	AUTO_INCREMENT,
    patient_first_name 	  	VARCHAR(50)		  NOT NULL,
    patient_last_name	    VARCHAR(50)		  NOT NULL,
    PRIMARY KEY (id)
) ENGINE = InnoDB;