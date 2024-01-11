#
# @author Wickramasekara T.M.A.M
# @email it19016962@my.sliit.lk
#

import numpy as np
from flask import Flask, request, jsonify
import pickle
from service.diseaseQuery import *

# Create flask app
app = Flask(__name__)

# Load the pickle model
model = pickle.load(open("final_model.pkl", "rb"))


@app.route('/', methods=['GET'])
def test_api():
    return "server started ..."

@app.route("/disease/predict", methods=["POST"])
def predict():
    int_features = []
    json_ = request.get_json()
    for key, value in json_[0].items():
        int_features.append(float(value))

    save_symptoms_details(int_features[0], int_features[1], int_features[2], int_features[3], int_features[4], int_features[5], 
    int_features[6], int_features[7], int_features[8], int_features[9], int_features[10], int_features[11], int_features[12], 
    int_features[13], int_features[14], int_features[15], int_features[16], int_features[17], int_features[18], int_features[19], 
    int_features[20], int_features[21], int_features[22])

    features = [np.array(int_features)]
    prediction = model.predict(features)

    if prediction == 0:
        return jsonify({"prediction_text": ' You do not Have Lung cancer or Tuberculosis'})
    elif prediction == 1:
        return jsonify({"prediction_text": ' You Have 75% Probability to Having Lung cancer'})
    else:
        return jsonify({"prediction_text": ' You Have 75% Probability to Having Tuberculosis'})

if __name__ == "__main__":
    app.run(debug=True,port=4000)
