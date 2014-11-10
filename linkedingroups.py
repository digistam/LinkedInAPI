import oauth2 as oauth
import time
from time import sleep
import linkedincredentials
import json

url = "http://api.linkedin.com/v1/groups/4444257:(id,name,site-group-url,posts:(id,title,summary,creator))?format=json"

consumer = oauth.Consumer(key = linkedincredentials.CONSUMER_KEY,secret = linkedincredentials.CONSUMER_SECRET)
     
token = oauth.Token(key = linkedincredentials.USER_TOKEN,secret = linkedincredentials.USER_SECRET)

client = oauth.Client(consumer, token)

resp, content = client.request(url)

items = json.loads(content)
total = items['posts']['_total']
print 'het totaal aantal: ' + str(total)
offset = 0
while offset < int(total) + 1:
    nexturl = "http://api.linkedin.com/v1/groups/4444257:(id,name,site-group-url,posts:(id,title,summary,creator))?start= " + str(offset) + "&count=25&format=json"
    resp, nextcontent = client.request(nexturl)
    items = json.loads(nextcontent)
    entity = []
    for item in items['posts']['values']:
        print item['summary']
    offset += 25
    print 'de offset is: ' + str(offset)
    sleep(5)
