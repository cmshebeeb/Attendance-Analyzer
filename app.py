from flask import Flask, render_template, request, jsonify
from Attendance import percent, num_class
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model_path = 'models/attendance_model.pkl'
model = joblib.load(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    total_classes = int(request.form['totalClasses'])
    attended_classes = int(request.form['attendedClasses'])
    attendance_percentage = percent(attended_classes, total_classes)
    
    safe_attendance_message = num_class(attended_classes, total_classes)
    
    return render_template('index.html', percentage=attendance_percentage, message=safe_attendance_message)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = pd.DataFrame(data)
    prediction = model.predict(features)
    return jsonify(prediction.tolist())

if __name__ == "__main__":
    app.run(debug=True)
