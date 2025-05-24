from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np
app = Flask(__name__)
data = pd.read_csv('Cleaned_data.csv')
import pprint

with open('RidgeModel.pkl', 'rb') as f:
    pipe = pickle.load(f)


@app.route('/')
def index():
    locations = sorted(data['location'].unique())
    return render_template('index.html', locations = locations)

@app.route('/predict', methods = ['POST'])
def predict():
    location = request.form.get('location')
    bhk = request.form.get('bhk')
    bath = request.form.get('bath')
    sqrt = request.form.get('total_sqft')

    print(location, bhk, bath, sqrt)
    input = pd.DataFrame([[location, bhk, bath, sqrt]], columns = ['location', 'bhk', 'bath', 'total_sqft'])
    prediction = pipe.predict(input)[0]*1e5  # Convert to lakhs 

    return str(np.round(prediction,2)) + ' Lakhs'

if __name__ == "__main__":
    app.run(debug=True , port=5000)