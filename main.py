from flask import Flask, render_template, request, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

# Serve the frontend
@app.route('/')
def home():
    return render_template('index.html')

# Serve static files (CSS, JS, images)
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

# API route to get analytics data
@app.route('/get-analytics/<int:user_id>')
def get_analytics(user_id):
    # Replace this with real database queries
    analytics_data = {
        "study_hours": 12,
        "syllabus_completion": 75
    }
    return jsonify(analytics_data)

# API route to submit feedback
@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    feedback = data.get("feedback")

    # Store feedback in a database (or log it for now)
    print(f"Feedback received from {name}: {feedback}")

    return jsonify({"message": "Feedback submitted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
