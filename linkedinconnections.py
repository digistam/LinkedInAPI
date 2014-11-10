import oauth2 as oauth
import time
import linkedincredentials
import json

url = "http://api.linkedin.com/v1/people/~/connections?format=json"

consumer = oauth.Consumer(
     key = linkedincredentials.CONSUMER_KEY,
     secret = linkedincredentials.CONSUMER_SECRET)
     
token = oauth.Token(
     key = linkedincredentials.USER_TOKEN, 
     secret = linkedincredentials.USER_SECRET)

client = oauth.Client(consumer, token)

resp, content = client.request(url)
items = json.loads(content)
entity = []
for item in items['values']:
    print item['firstName'] + ' ' + item['lastName']
    try:
        print item['industry']
    except KeyError:
        print ''
    try:
        print item['headline']
    except KeyError:
        print ''
    try:
        print 'url: ' + item['siteStandardProfileRequest']['url']
    except KeyError:
        print ''
    try:
        print 'picture: ' + item['pictureUrl']
    except KeyError:
        print 'no picture'
    try:
        print 'country: ' + item['location']['country']['code']
    except KeyError:
        print 'no location'
    try:
        print 'location: ' + item['location']['name']
    except KeyError:
        print 'no location'
    try:
        print 'distance: ' + item['distance']
    except KeyError:
        print ''
#   try:
#       print 'public profile: ' + entity[i]['publicProfileUrl']
#   except KeyError:
#       print 'no public profile'
#   print entity[i]['numFollowers']
#   try:
#       print entity[i]['status']
#   except KeyError:
#       print 'no status'
