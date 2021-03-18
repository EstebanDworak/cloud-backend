from cloudant import Cloudant
from flask import Flask, render_template, request, jsonify
import atexit
import os
import json
import json
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(os.environ.get('API_KEY',""))
tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    authenticator=authenticator
)
tone_analyzer.set_service_url(os.environ.get('API_URL',""))

app = Flask(__name__, static_url_path='')

port = int(os.getenv('PORT', 8000))

@app.route('/', methods=['POST'])
def root():
    content = request.json
    
    text = content["text"]

    tone_analysis = tone_analyzer.tone(
        {'text': text},
        content_type='application/json'
    ).get_result()


    return tone_analysis


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)