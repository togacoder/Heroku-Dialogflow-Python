from flask import Flask, request
import json
import requests

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    # SpreadSheets URL
    url = 'https://script.google.com/macros/s/AKfycbyWIu6E1aH_NGNJfNSCCdqCdbwXopzmQxvO91nlcGugASqWrcc/exec'
    message = request;
    res = requests.post(url, json.dumps(message)) 

    message = message.json.get("queryResult").get("parameters").get("message")
    if message == "hello":
        response = {
            "payload": {
                "google": {
                    "expectUserResponse": True,
                    "richResponse": {
                        "items": [
                            {
                                "simpleResponse": {
                                    "textToSpeech": "Hello World." 
                                }
                            }
                        ]
                    }
                }
            }
        }
    else:
        response = {
            "payload": {
                "google": {
                    "expectUserResponse": True,
                    "richResponse": {
                        "items": [
                            {
                                "simpleResponse": {
                                    "textToSpeech": "Hello Heroku." 
                                }
                            }
                        ]
                    }
                }
            }
        }
    
    # SpreadSheetsにPost
    res = requests.post(url, json.dumps(response))

    return json.dumps(response) 
