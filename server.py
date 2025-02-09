'''We first import all the modules and the functions neededd'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

'''We define a route for emotion detector'''
@app.route("/emotionDetector")
def emo_detector():
    '''Here we define the backend view or the function fro thee emotionDetection route'''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response is None:
        return "Invalid text! Please try again!."
    return f"""For the given statement, the system response is
    'anger': {response['anger']}, 
    'disgust': {response['disgust']},
    'fear': {response['fear']},
    'joy': {response['joy']} 
    and 'sadness': {response['sadness']}.
    The dominant emotion is {response['dominant_emotion']}."""

@app.route("/")
def render_index_page():
    '''This renders the main page or the home page'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
