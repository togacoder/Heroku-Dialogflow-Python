# -*- coding: utf8 -*-

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

    post_SpreadSheets(displayName.encode('utf-8'))
    post_SpreadSheets(message.encode('utf-8'))

    # 会話の制御
    # message = 'レスポンス'
    if displayName == '帰宅時1':
        message = 'お帰りなさい。'
    elif displayName == '帰宅時2':
        message = 'お疲れ様です。'
    elif displayName == 'Default Welcome Intent':
        message = 'Start Dialogflow'
    elif displayName == 'Default Fallback Intent':
        message = 'もう一度お願いします。'
    elif displayName == 'Exit':
        message = 'Outing Agentを終了します。'
    
    res = res_json(message)
    post_SpreadSheets(message.encode('utf-8'))

    # Dialogflow に返す
    return json.dumps(res) 


# Dialogflow に返すjsonを作成
def res_json(message):
    res = {
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
    return res


# Google SpreadSheets にPOSTする
def post_SpreadSheets(data):
    # Outing URL
    url = 'https://script.google.com/macros/s/AKfycbze93rXUHBp1vcHF5GQLxUqbgPrQeNjGwCOBCFYleBaZNiJm3_C/exec'
    res = requests.post(url, json.dumps(data)) 


if __name__ == '__main__':
    app.run(host="localhost")
