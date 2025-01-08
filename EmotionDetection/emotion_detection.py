import requests
import json

def emotion_detector(text_to_analyse):  # Define a function named emotion_detector that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the emotion analysis service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        # Extracting emotions from the response
        emotions        = formatted_response['emotionPredictions'][0]['emotion']
        anger_score     = emotions['anger']
        disgust_score   = emotions['disgust']
        fear_score      = emotions['fear']
        joy_score       = emotions['joy']
        sadness_score   = emotions['sadness']
        dominant_emotion= max(emotions, key=emotions.get)
    # If the response status code is 400, set emotions to None
    elif response.status_code == 400:
        emotions        = None
        anger_score     = None
        disgust_score   = None
        fear_score      = None
        joy_score       = None
        sadness_score   = None
        dominant_emotion= None

    # Returning a dictionary containing sentiment analysis results
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
