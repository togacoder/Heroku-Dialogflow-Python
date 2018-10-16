from flask import Flask, request
import json
import requests

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    message = request.json.get("queryResult").get("parameters").get("message");
    post_SpreadSheets(message)

    # 会話の制御
    if message == 'hello':
        message = 'Hello, World!!' 
    else:
        message = 'hello, Heroku.'
    
    response = res_json(message)
    post_SpreadSheets(message)

    # Dialogflow に返す
    return json.dumps(response) 


# Dialogflow に返すjsonを作成
def res_json(message):
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
    return response


# Google SpreadSheets にPOSTする
def post_SpreadSheets(data):
    url = 'https://script.google.com/macros/s/AKfycbyWIu6E1aH_NGNJfNSCCdqCdbwXopzmQxvO91nlcGugASqWrcc/exec'
    res = requests.post(url, json.dumps(data))    


if __name__ == '__main__':
    app.run(host="localhost")
