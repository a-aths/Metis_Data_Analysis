from flask import Flask, request, render_template
import pandas as pd
import joblib


app = Flask(__name__)
@app.route('/', methods=['GET', "POST"])
def main():
    if request.method == 'POST':
        clf=joblib.load('rf_clf.pkl')
        Pregnancies = request.form.get("Pregnancies")
        Glucose= request.form.get("Glucose")
        BloodPressure = request.form.get("BloodPressure")
        BMI = request.form.get("BMI")
        DiabetesPedigreeFunction = request.form.get("DiabetesPedigreeFunction") or None
        Age = request.form.get('Age')

        X = pd.DataFrame(
            [[Pregnancies, Glucose, BloodPressure, BMI, 
            DiabetesPedigreeFunction, Age]], columns = ["Pregnancies", "Glucose", 
            "BloodPressure", "BMI", "DiabetesPedigreeFunction", "Age"])
        prediction = clf.predict(X)[0]
        if prediction == 1:
            prediction = 'Diabetes II Likely'
        else:
            prediction = 'Diabetes II Unlikely'

    else:
        prediction = ''
    return render_template(
        'diabetes_frontend.html', output=prediction)

if __name__ == '__main__':
    app.run(debug=True)