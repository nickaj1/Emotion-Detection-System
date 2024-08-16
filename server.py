from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector():
    # Getting query from the user
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)
    




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)