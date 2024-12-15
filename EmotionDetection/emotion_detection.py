import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse} }

    response = requests.post(url, json= myobj, headers=header, timeout=30)
    
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']

    emotions = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness
    }

    dominant_emotion = None
    for emotion, score in emotions.items():
        if score >= 0.6:
            dominant_emotion = emotion
            break

    result = {
        "emotions": emotions,
        "dominant_emotion": dominant_emotion
    }

    print(result)
    
    return result


# from emotion_detection import emotion_detector
# emotion_detector("i am happy")
# emotion_detector("I am sad")