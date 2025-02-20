'''server file'''
from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_detector():
    '''using sent_detector funtion'''
    text_to_analyze = request.args.get('textToAnalyze', '')

    response = emotion_detector(text_to_analyze)

    # Check if dominant_emotion is None
    if response.get("dominant_emotion") is None:
        return jsonify({"error": "Invalid text! Please try again!"})

    return jsonify(response)  # Convert response to JSON and return


@app.route("/")
def render_index_page():
    '''render the template'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5009)
