'''Emotion Detection Code'''

import json  # Standard import should be first
import requests  # Third-party imports come after standard imports

def emotion_detector(text_to_analyze):
    '''Function to analyze emotions in the given text'''
    
    url = ('https://sn-watson-emotion.labs.skills.network/'
           'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict')
    myobj = {"raw_document": {"text": text_to_analyze}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Handling blank input
    if not text_to_analyze.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    try:
        response = requests.post(url, json=myobj, headers=header, timeout=10)

        # Handle API returning a 400 error
        if response.status_code == 400:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None
            }

        response_dict = response.json()  # Directly parse JSON response

        # Extract emotion data safely
        emotion_data = response_dict.get('emotionPredictions', [{}])[0].get('emotion', {})

        # Find the dominant emotion
        dominant_emotion = max(emotion_data, key=emotion_data.get, default=None)

        # Return formatted dictionary with emotions and dominant emotion
        return {
            "anger": emotion_data.get('anger'),
            "disgust": emotion_data.get('disgust'),
            "fear": emotion_data.get('fear'),
            "joy": emotion_data.get('joy'),
            "sadness": emotion_data.get('sadness'),
            "dominant_emotion": dominant_emotion
        }

    except requests.RequestException as e:
        return {"error": f"API request failed: {str(e)}"}
