from flask import Flask, jsonify, render_template, request
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

with open('xgb_model.pkl', 'rb') as file:
    model = pickle.load(file)
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)
app = Flask(__name__)
weather = ['Cloudy', 'Rainy', 'Snowy', 'Sunny']
@app.route('/')
def index():
    return render_template('form.html')


@app.route('/predict', methods=['POST'])
def predict():
    x_predict = {
        'temp': float(request.form['temp']),
        'humidity': float(request.form['humidity']),
        'wind_speed': float(request.form['wind_speed']),
        'precipitation': float(request.form['precipitation']),
        'cloud_cover': int(request.form['cloud_cover']),
        'atmospheric_pressure': float(request.form['atmospheric_pressure']),
        'uv_index': float(request.form['uv_index']),
        'season': int(request.form['season']),
        'visibility': float(request.form['visibility']),
        'location': int(request.form['location'])
    }

    features = np.array([[x_predict['temp'], x_predict['humidity'], x_predict['wind_speed'],
                          x_predict['precipitation'], x_predict['cloud_cover'],
                          x_predict['atmospheric_pressure'], x_predict['uv_index'],
                          x_predict['season'],x_predict['visibility'] ,x_predict['location']]])
    features= scaler.transform(features)

    prediction = model.predict(features)
      # Assuming the model outputs probabilities

    return render_template('result.html', weather=weather[prediction[0]])


if __name__ == '__main__':
    app.run(debug=True)

