"""Flask web server for emotion detection application."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detect():
    """Handle emotion detection requests and return the system's response."""
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    emotions = response['emotions']
    dominant = response['dominant_emotion']

    if dominant is None:
        return "Invalid input! Try again."
    return (
        f"For the given statement, the system response is {emotions}. "
        f"The dominant emotion is {dominant}"
    )

@app.route("/")
def render_index():
    """Render the index.html page."""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
    