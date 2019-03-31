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
	id 								INT 			  	NOT NULL 	  	AUTO_INCREMENT		PRIMARY KEY,
    first_name 	  					VARCHAR(32)		  	NOT NULL,
    middle_initial					CHAR(2), 
    last_name	    				VARCHAR(32)		  	NOT NULL,
    jr_sr							CHAR(3),				
    sex_id							TINYINT				NOT NULL,
    dob								DATE,
    health_card_number				CHAR(12),
    province_or_territory_issued	CHAR(2),
    case_record_number				INT,
    province_or_territory			CHAR(2),
    postal_code						CHAR(7),
    facility_or_agency_id			INT,
    primary_language_code			CHAR(3),
    interpreter_need				TINYINT,
    reasons_for_referral			TEXT,
    last_updated 					TIMESTAMP	  	  	DEFAULT 		CURRENT_TIMESTAMP 			ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY fk_primary_language (primary_language_code)
		REFERENCES primary_language (primary_language_code),
    FOREIGN KEY fk_sex (sex_id)
		REFERENCES sex(id)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS screener_instance (
	id 							INT 			  	NOT NULL 	  	AUTO_INCREMENT		PRIMARY KEY,
    patient_id					INT					NOT NULL,
    assessor					VARCHAR(64), 
    self_reported_health 		SMALLINT,
    assessment_urgency_score	TINYINT,
    assessment_required			CHAR(3),
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

INSERT INTO patient (id, first_name, middle_initial, last_name, jr_sr, sex_id, dob, health_card_number, province_or_territory_issued, 
	case_record_number, province_or_territory, postal_code, facility_or_agency_id, primary_language_code, interpreter_need, reasons_for_referral,
    last_updated) VALUES
(default, "Mike", "J.", "Lukina", NULL, 1, "1990-03-15", "GMLEK2KW8G83", "ON", 777, "ON", "N2R 2F3", 1234, "eng", 1, "dementia", default),
(default, "Tony", "P.", "Lukina", NULL, 2, "1992-04-03", "4Q525DXFNMRL", "BC", 888, "BC", "R3Y E2U", 5678, "fre", 2, "depression", default);

INSERT INTO screener_instance (id, patient_id, assessor, self_reported_health, assessment_urgency_score, assessment_required) VALUES
(default, 2, "Peter Madziak", 0, 2, "No");