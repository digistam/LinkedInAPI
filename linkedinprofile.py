import oauth2 as oauth
import time
import linkedincredentials

url = "http://api.linkedin.com/v1/people/~?format=json"

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