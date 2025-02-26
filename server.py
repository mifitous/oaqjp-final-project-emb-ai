"""
server.py

This module handles the main server logic, including routing, request handling, 
and response generation.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """
    Processes the default page

    Returns:
        str: A default html page
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Processes the emotion data to extract insights.

    Returns:
        str: A summary of the dominant emotion.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    anger   = response['anger']
    disgust = response['disgust']
    fear    = response['fear']
    joy     = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Check if the dominant_emotion is None, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    # Return a formatted string with the sentiment label and score
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
