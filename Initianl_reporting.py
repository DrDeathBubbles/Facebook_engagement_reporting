import requests
from requests_oauthlib import OAuth1
import os

#r = requests.get('https://graph.facebook.com/v2.8/WebSummitHQ/feed',
#        headers = {'access_token':os.environ['ACCESSTOKEN']})
#

r = requests.get('https://graph.facebook.com/v2.8/WebSummitHQ/feed?access_token={}'.format(os.environ['ACCESSTOKEN']))


print(r.text)
