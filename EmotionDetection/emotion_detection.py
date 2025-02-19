import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Send the POST request to the API
    response = requests.post(url, json=myobj, headers=header)
    
    # Print the raw response text for debugging
    print("Raw Response:", response.text)
    
    # Parse the response JSON into a dictionary
    response_dict = json.loads(response.text)
    
    # Extract emotions dictionary from the response
    emotion_data = response_dict['emotionPredictions'][0]['emotion']
    
    # Assign emotion scores to variables
    anger_score = emotion_data.get('anger', 0)
    disgust_score = emotion_data.get('disgust', 0)
    fear_score = emotion_data.get('fear', 0)
    joy_score = emotion_data.get('joy', 0)
    sadness_score = emotion_data.get('sadness', 0)
    
    # Create a dictionary of emotions and scores
    emotions_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    # Find the dominant emotion (highest score)
    dominant_emotion = max(emotions_scores, key=emotions_scores.get)
    
    # Include dominant emotion in the output dictionary
    emotions_scores['dominant_emotion'] = dominant_emotion
    
    return emotions_scores


