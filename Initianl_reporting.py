import requests
import os
import json
import pdb
#r = requests.get('https://graph.facebook.com/v2.8/WebSummitHQ/feed',
#        headers = {'access_token':os.environ['ACCESSTOKEN']})


def get_likes(post_id):
    number_of_likes = 0
    r = requests.get('https://graph.facebook.com/v2.8/{}/likes?access_token={}'.format(post_id,os.environ['ACCESSTOKEN']))
    data = json.loads(r.text)
    number_of_likes = number_of_likes + len(data['data'])
    while 'next' in data['paging'].keys():
        data = requests.get(data['paging']['next'])
        data = json.loads(data.text)
        number_of_likes = number_of_likes + len(data['data'])
    return number_of_likes


def get_likes_temp(post_id):
    number_of_likes = 0
    r = requests.get('https://graph.facebook.com/v2.8/{}/likes?access_token={}'.format(post_id,os.environ['ACCESSTOKEN']))
    data = json.loads(r.text)
    return data 

def post_information(post_id):
    r = requests.get('https://graph.facebook.com/v2.8/{}?access_token={}'.format(post_id,os.environ['ACCESSTOKEN']))
    data = json.loads(r.text)
    return data

#Initial request for posts from WebSummit page
r = requests.get('https://graph.facebook.com/v2.8/WebSummitHQ/feed?access_token={}'.format(os.environ['ACCESSTOKEN']))
data = json.loads(r.text)
r = requests.get('http://graph.facebook.com/v2.8/')





print(data)
