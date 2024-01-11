#
# @author Wickramasekara T.M.A.M
# @email it19016962@my.sliit.lk
#

from config.dbConfig import insert

# Data Insert Query
def save_symptoms_details(age, gender, air_pollution, alcohol_use, dust_allergy, occuPational_hazards, genetic_risk, chronic_lung_disease, balanced_diet, obesity, smoking, passive_smoker, chest_pain, coughing_of_blood, fatigue, weight_loss, shortness_of_breath, wheezing, swalHealthying_difficulty, clubbing_of_finger_nails, frequent_cold, dry_cough, snoring):
    sql_query = """INSERT INTO disease_symptoms (age, gender, air_pollution, alcohol_use, dust_allergy, occuPational_hazards, genetic_risk, chronic_lung_disease, balanced_diet, obesity, smoking, passive_smoker, chest_pain, coughing_of_blood, fatigue, weight_loss, shortness_of_breath, wheezing, swalHealthying_difficulty, clubbing_of_finger_nails, frequent_cold, dry_cough, snoring) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    args = (age, gender, air_pollution, alcohol_use, dust_allergy, occuPational_hazards, genetic_risk, chronic_lung_disease, balanced_diet, obesity, smoking, passive_smoker, chest_pain, coughing_of_blood, fatigue, weight_loss, shortness_of_breath, wheezing, swalHealthying_difficulty, clubbing_of_finger_nails, frequent_cold, dry_cough, snoring)
    result = insert(sql_query, args)
    return result
    


