CREATE DATABASE IF NOT EXISTS pc_screener;

USE pc_screener;

CREATE TABLE IF NOT EXISTS screener_instance (
	id 				INT 			  NOT NULL 	  	AUTO_INCREMENT,
    first_name 	  	VARCHAR(50)		  NOT NULL,
    last_name	    VARCHAR(50)		  NOT NULL,
    time_recorded 	TIMESTAMP	  	  DEFAULT 		CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
) ENGINE = InnoDB;