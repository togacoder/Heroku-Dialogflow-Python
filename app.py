from flask import Flask, request
import json
import requests

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    # parameters : Dialogflowで設定した変数名
    # queryText : 音声認識した文字列
    # message = request.json.get("queryResult").get("parameters").get("message");
    message = request.json.get("queryResult").get("queryText");

    # Intent Name
    displayName = request.json.get("queryResult").get("intent").get("displayName")

    post_SpreadDheets(displaynName)
    post_SpreadSheets(message)

    # 会話の制御
    # message = 'レスポンス'
    if displayName == '帰宅時1':
        message = 'お帰りなさい。'
    elif dispalyName == '帰宅時2':
        message = 'お疲れ様です。'
    elif dispalyName == 'Default Fallback Intent':
        message = 'もう一度お願いします。'
    
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
