import requests
import json


def emotion_detector(text_to_analyze):
    try:
        url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

        header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

        myobj =  { "raw_document": { "text": text_to_analyze } }

        response = requests.post(url , headers=header, json=myobj)

        # Converting the response text into a dictionary using the json library functions.
        formatted_response = json.loads(response.text)

        # Extracting the required set of emotion
        emotions = formatted_response['emotionPredictions'][0]['emotion']

        # Finding which emotion with the highest score.
        highest_score = float('-inf')
        for emotion, score in emotions.items():
            if score > highest_score:
                highest_score = score
                dominant_emotion = emotion
        
        # Returning the following output format.
        result = {
                'anger': emotions['anger'],
                'disgust': emotions['disgust'],
                'fear': emotions['fear'],
                'joy': emotions['joy'],
                'sadness': emotions['sadness'],
                'dominant_emotion': dominant_emotion
                }      
        return result
    
    except NameError:
        return {'message':'review code well!'}
