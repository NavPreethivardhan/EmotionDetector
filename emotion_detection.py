import requests 

def emotion_detector(text_to_analyse):  
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' 
    jsonobj = { "raw_document": { "text": text_to_analyse } } 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
    response = requests.post(URL, json = jsonobj, headers=header) 
    return response.text 