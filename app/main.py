import flask
import os
import requests
app = flask.Flask(__name__)
api_key = os.environ.get('KEY')

endpoint = "https://api.bing.microsoft.com/v7.0/SpellCheck"

params = {
    'mkt':'en-us',
    'mode':'proof'
    }
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Ocp-Apim-Subscription-Key': api_key,
    }

@app.route('/',methods=['POST', 'GET'])
def hello_world():
  if flask.request.method == 'POST':
    data = {'text': flask.request.form.get('text')}
    response = requests.post(endpoint, headers=headers, params=params, data=data)
    json_response = response.json() 
    return json_response
  else:
    return flask.render_template('index.html')


"""

import requests

url = "https://api.promptapi.com/paraphraser"

payload = "body".encode("utf-8")
headers= {
  "apikey": "aMERAsVUOlQXKYTuiMMOd5QfmgYSRkb1"
}

response = requests.request("POST", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
"""

#fc2557f8-48e7-49dd-ac18-494dd1a242c4
#6b5d31ae-17de-4f73-abe8-b3d39b904018