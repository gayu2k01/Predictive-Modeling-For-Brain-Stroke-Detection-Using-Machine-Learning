from flask import Flask, render_template, request
import pickle
import numpy as np

model1 = pickle.load(open(r'C:\Users\gayat\Desktop\GAYU PROJECT\project final\stroke.pkl', 'rb'))  


app = Flask(__name__)  # initializing Flask app

@app.route("/", methods=['GET'])
def hello():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST': 
        d2 = request.form['gender']
        d3 = request.form['age']
        d4 = request.form['hypertension']
        d5 = request.form['heart_disease']
        d6 = request.form['ever_married']
        d7 = request.form['work_type']
        d8 = request.form['Residence_type']
        d9 = request.form['avg_glucose_level']
        d10 = request.form['bmi']
        d11 = request.form['smoking_status']
        
        arr = np.array([[d2, d3, d4, d5, d6, d7, d8, d9, d10, d11]])
        print([d2, d3, d4, d5, d6, d7, d8, d9, d10, d11])
        pred1 = model1.predict(arr)
        print(pred1)
        
        if pred1 == 1:
            prediction_text1 = "Brain Stroke Occur"
        else:
            prediction_text1 = "Brain Stroke Does Not Occurs"

    return render_template('result.html', prediction_text1=prediction_text1)
    
if __name__ == '__main__':
    app.run(debug=False)
