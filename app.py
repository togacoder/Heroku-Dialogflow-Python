from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    message = request.json.get("queryResult").get("parameters").get("message")
    if message == "hello":
        response = {
            "payload": {
                "google": {
                    "expectUserResponse": True,
                    "richResponse": {
                        "items": [
                            {
                                "simpleResponse": {
                                    "textToSpeech": message 
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
                                    "textToSpeech": "else" 
                                }
                            }
                        ]
                    }
                }
            }
        }

    return json.dumps(response)
