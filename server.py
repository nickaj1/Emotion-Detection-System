from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/emotionDetector')
def emotion_detect():
    # Getting query from the user
    text_to_analyze = request.args.get('textToAnalyze')

    # Calling the emotion detector function and parsing the text to be analysed
    response = emotion_detector(text_to_analyze)

     # Handling error when input text is empty
    if response['dominant_emotion'] is None:
        return {'message': 'Invalid text! Please try again!'}

    # Analysed text reponses
    result =  {
            "anger": response['anger'],
            "disgust": response['disgust'],
            "fear": response['fear'],
            "joy": response['joy'],
            "sadness": response['sadness'],
            "The dominant emotion is": response['dominant_emotion']
        }
    
    
    # Returning final result
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)