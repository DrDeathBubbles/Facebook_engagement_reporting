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


def post_information_link(post_id):
    r = requests.get('https://graph.facebook.com/v2.8/{}/?fields=link&access_token={}'.format(post_id,os.environ['ACCESSTOKEN']))
    data = json.loads(r.text)
    return data['link']


def post_information(post_id):
    r = requests.get('https://graph.facebook.com/v2.8/{}?access_token={}'.format(post_id,os.environ['ACCESSTOKEN']))
    data = json.loads(r.text)
    return data

def page_insights(post_id):
    r = requests.get('https://graph.facebook.com/v2.8/{}/insights/page_impressions_unique?access_token={}'.format(post_id,os.environ['ACCESSTOKEN']))
    data = json.loads(r.text)
    return data


def post_insights(page_id,post_id):
    r = requests.get('https://graph.facebook.com/v2.8/{}_{}/insights/post_impressions?access_token={}'.format(page_id,post_id,os.environ['ACCESSTOKEN']))
    data = json.loads(r.text)
    return data


def post_insights_2(page_id,post_id):
    r = requests.get('https://graph.facebook.com/v2.8/{}/insights/post_impressions?access_token={}'.format(post_id,os.environ['ACCESSTOKEN']))
    data = json.loads(r.text)
    return data


#Initial request for posts from WebSummit page
r = requests.get('https://graph.facebook.com/v2.8/WebSummitHQ/feed?access_token={}'.format(os.environ['ACCESSTOKEN']))
data = json.loads(r.text)
#r = requests.get('http://graph.facebook.com/v2.8/')

#Kerry



print(data)
