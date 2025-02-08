import requests

# Define the features for prediction
data = {
    "Roll\nNo.": [1],
    "absent_ratio": [0.1],
    "absent_days": [3],
    "Curent Month's Lect.": [5],
    "Overall Lect.": [10],
    "present_ratio": [0.9],
    "present_days": [9],
    "attendance_category_high": [1],
    "attendance_category_medium": [0],
    "attendance_category_low": [0]
}

response = requests.post('http://127.0.0.1:5000/predict', json=data)
print(response.json())
