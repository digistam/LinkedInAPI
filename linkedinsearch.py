import oauth2 as oauth
import time
import linkedincredentials
import sys

#url = "http://api.linkedin.com/v1/people/~/connections?format=json"
try:
    _title = sys.argv[1]
except IndexError:
    print 'usage: python linkedinpeople.py <keyword>'
    sys.exit()
url = "http://api.linkedin.com/v1/people-search:(people:(first-name,last-name,headline))?title=" + _title + "&format=json&count=25"

consumer = oauth.Consumer(
     key = linkedincredentials.CONSUMER_KEY,
     secret = linkedincredentials.CONSUMER_SECRET)
     
token = oauth.Token(
     key = linkedincredentials.USER_TOKEN, 
     secret = linkedincredentials.USER_SECRET)

client = oauth.Client(consumer, token)

resp, content = client.request(url)
print resp
print content
