"""
This module defines a Flask application that provides an API for emotion detection.
"""

from flask import Flask, request, render_template, jsonify
from EmotionDetection.emotion_detection import emotion_detector

#Creating Flask App
app = Flask(__name__)

@app.route('/')
def render_page():
    """
    Render the main page.
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def dominant_emotion_detector():
    """
    Detect the dominant emotion in the provided text.
    """
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    formatted_response = jsonify(response)

    # Check if dominant_emotion is None
    if response['dominant_emotion'] is None:
        return {"message": "Invalid text! Please try again!"}, 200
    return formatted_response

# Runing the app
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
# End of server.py module
    