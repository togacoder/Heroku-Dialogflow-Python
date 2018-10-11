import requests

url = 'https://script.google.com/macros/s/AKfycbyWIu6E1aH_NGNJfNSCCdqCdbwXopzmQxvO91nlcGugASqWrcc/exec'
response = requests.post(url, data = { 'queryText': 'data1', 'fulfillmentText': 'data2' })
print(response.status_code)
print(response.text)
