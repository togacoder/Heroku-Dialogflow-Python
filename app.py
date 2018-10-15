from flask import Flask, request
import json
import requests

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    # queryResult.queryText : 認識文字列
    # parameters : 変数
    message = request.json.get("queryResult").get("parameters").get("message");
    data = request.json
    post_SpreadSheets(data)
    
    if message == 'hello':
        message = 'Hello, World!!' 
    else:
        message = 'hello, Heroku.'
    
    response = make_json(message)

    post_SpreadSheets(response)

    return json.dumps(response) 

def make_json(message):
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

def post_SpreadSheets(data):
    url = 'https://script.google.com/macros/s/AKfycbyWIu6E1aH_NGNJfNSCCdqCdbwXopzmQxvO91nlcGugASqWrcc/exec'
    res = requests.post(url, json.dumps(data))    

if __name__ == '__main__':
    app.run(host="localhost")
