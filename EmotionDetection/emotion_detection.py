import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse} }

    response = requests.post(url, json= myobj, headers=header, timeout=30)

    if response.status_code == 200:
        try:
            formatted_response = response.json()

            anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
            disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
            fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
            joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
            sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        except:
            anger = disgust = fear = joy = sadness = None
    elif response.status_code > 200:
        anger = disgust = fear = joy = sadness = None

    emotions = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness
    }

    dominant_emotion = None
    for emotion, score in emotions.items():
        if score and score >= 0.6:
            dominant_emotion = emotion
            break

    result = {
        "emotions": emotions,
        "dominant_emotion": dominant_emotion
    }
    
    return result