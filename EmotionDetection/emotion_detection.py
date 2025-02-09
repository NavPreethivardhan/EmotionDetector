import requests 
import json

def emotion_detector(text_to_analyse):  
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' 
    jsonobj = { "raw_document": { "text": text_to_analyse } } 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
    response = requests.post(URL, json = jsonobj, headers=header) 
    formatted_response = json.loads(response.text)

    if response.status_code==200:
        formatted_dict = formatted_response['emotionPredictions'][0]["emotion"]
        anger_score = formatted_dict['anger']
        disgust_score = formatted_dict['disgust']
        fear_score = formatted_dict['fear']
        joy_score = formatted_dict['joy']
        sadness_score = formatted_dict['sadness']
        dominant_emotion = max(formatted_dict, key=formatted_dict.get)
        return{'anger': anger_score,'disgust': disgust_score,'fear': fear_score,'joy': joy_score,'sadness': sadness_score,'dominant_emotion': dominant_emotion }
    elif response.status_code == 500:
        return{'anger': None,'disgust': None,'fear': None,'joy': None,'sadness': None,'dominant_emotion': None }
    