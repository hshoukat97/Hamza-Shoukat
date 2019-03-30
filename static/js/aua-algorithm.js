function get_self_reliance_index() {
  var cognitive_skills_value = parseInt(document.getElementById("cognitive-skills").value);
  var bathing_value = parseInt(document.getElementById("bathing").value);
  var personal_hygiene_value = parseInt(document.getElementById("personal-hygiene").value);  
  var dressing_lower_body_value = parseInt(document.getElementById("dressing-lower-body").value);
  var locomotion_value = parseInt(document.getElementById("locomotion").value);

  if (cognitive_skills_value === 1 || bathing_value === 1 || 
      personal_hygiene_value === 1 || dressing_lower_body_value === 1 ||
      locomotion_value === 1) {
    return self_reliant = false;
  }
  else {
    return self_reliant = true;
  }
}

function get_self_reported_health_value() {
  var self_reported_health_value = parseInt(document.getElementById("self-reported-health").value);
  
  if (self_reported_health_value === 0 || self_reported_health_value === 1) {
    return true; 
  }
  else {
    return false; 
  }
}

function get_dyspnea_value() {
  var dyspnea_value = parseInt(document.getElementById("dyspnea").value);

  if (dyspnea_value === 1 || dyspnea_value === 2 || dyspnea_value === 3) {
    return true;
  }
  else {
    return false;
  }
}

function get_unstable_value() {
  var instability_of_conditions_a_value = parseInt(document.getElementById("instability-of-conditions-a").value);

  if (instability_of_conditions_a_value === 1) {
    return true;
  }
  else {
    return false;
  }
}

function get_informal_helper_status() {
  var informal_helper_status_b_value = parseInt(document.getElementById("informal-helper-status-b").value);

  if (informal_helper_status_b_value === 1) {
    return true;
  }
  else {
    return false;
  }
}

function get_self_reported_mood_value() {
  var self_reported_mood_value = parseInt(document.getElementById("self-reported-mood").value);

  if (self_reported_mood_value === 1) {
    return true;
  }
  else {
    return false;
  }
}

function get_personal_hygiene_value() {
  var personal_hygiene_value = parseInt(document.getElementById("personal-hygiene").value);

  if (personal_hygiene_value === 1) {
    return true;
  }
  else {
    return false; 
  }
}

function get_assessment_urgency_score() {
  if (get_self_reliance_index() === true && get_self_reported_health_value() ===
      false && (get_dyspnea_value() === false && get_unstable_value() === false)) {
    return aua_score = 2;
  }
  else if (get_self_reliance_index() === true && get_self_reported_health_value() ===
            false && (get_dyspnea_value() === true || get_unstable_value() === true)) {
    return aua_score = 3;
  }
  else if (get_self_reliance_index() === true && get_self_reported_health_value() ===
            true && get_unstable_value() === false) {
    return aua_score = 1;
  }
  else if (get_self_reliance_index() === true && get_self_reported_health_value() ===
            true && get_unstable_value() === true) {
    return aua_score = 3;
  }
  else if (get_self_reliance_index() === false && get_informal_helper_status() === true) {
    return aua_score = 6;
  }
  else if (get_self_reliance_index() === false && get_informal_helper_status() === 
            false && get_self_reported_mood_value() === true) {
    return aua_score = 6;
  }
  else if (get_self_reliance_index() === false && get_informal_helper_status() === 
            false && get_self_reported_mood_value() === false && 
            get_personal_hygiene_value() === false) {
    return aua_score = 4;
  }
  else if (get_self_reliance_index() === false && get_informal_helper_status() === 
          false && get_self_reported_mood_value() === false && 
          get_personal_hygiene_value() === true) {
    return aua_score = 5;
  }
  else {
    return aua_score = "error";
  }
}

function calculate_aua_score() {
  console.log("self reliance index: " + get_self_reliance_index());
  console.log("self reported health value: " + get_self_reported_health_value());
  console.log("dyspnea value: " + get_dyspnea_value());
  console.log("unstable value: " + get_unstable_value());
  console.log("informal helper value: " + get_informal_helper_status());
  console.log("self reported mood value: " + get_self_reported_mood_value());
  console.log("personal hygiene value: " + get_personal_hygiene_value());
  console.log(get_assessment_urgency_score()); 
  
  if (get_assessment_urgency_score() >= 3) {
    alert("Your assessment urgency score is " + get_assessment_urgency_score() + 
      "\nThis patient requires a CHA assessment");
  }
  else {
    alert("Your assessment urgency score is " + get_assessment_urgency_score() + 
      "\nThis patient does not require a CHA assessment");
  }
}