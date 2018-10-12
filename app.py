from flask import Flask, request
import json
import requests

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    message = request.json.get("queryResult").get("parameters").get("message");

    response = ""
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
    
    post_SpreadSheets(response)

    return json.dumps(response) 

def post_SpreadSheets(response):
    url = 'https://script.google.com/macros/s/AKfycbyWIu6E1aH_NGNJfNSCCdqCdbwXopzmQxvO91nlcGugASqWrcc/exec'
    res = requests.post(url, json.dumps(response))    

if __name__ == '__main__':
    app.run(host="localhost")
