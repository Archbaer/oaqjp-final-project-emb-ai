from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detec():
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    emotions = response['emotions']
    dominant = response['dominant_emotion']

    if emotions is None:
        return "Invalid input! Try again."
    else:
        return "For the given statement, the system response is {}. The dominant emotion is {}".format(emotions, dominant)


@app.route("/")
def render_index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)