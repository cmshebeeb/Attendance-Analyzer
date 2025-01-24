from flask import Flask, render_template, request
from Attendance import percent, num_class

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)
