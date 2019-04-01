USE pc_screener;

SELECT * FROM patient;
SELECT * FROM screener_instance;

SELECT first_name, last_name, sex
FROM patient AS p
JOIN sex AS s
	ON s.id = p.sex_id;
    
SELECT p.id, p.first_name, p.last_name, s.assessor, s.assessment_urgency_score, s.assessment_required, s.date_time_completed
FROM patient AS p
JOIN screener_instance AS s
	ON p.id = s.patient_id
WHERE s.assessment_urgency_score >= 3
ORDER BY s.assessment_urgency_score DESC, date_time_completed ASC;