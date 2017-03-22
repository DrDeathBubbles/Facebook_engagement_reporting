import requests
import os
import json
#r = requests.get('https://graph.facebook.com/v2.8/WebSummitHQ/feed',
#        headers = {'access_token':os.environ['ACCESSTOKEN']})



r = requests.get('https://graph.facebook.com/v2.8/WebSummitHQ/feed?access_token={}'.format(os.environ['ACCESSTOKEN']))
data = json.loads(r.text)

print(data)
