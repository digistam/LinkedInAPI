import oauth2 as oauth
import time
import linkedincredentials
import sys
import json

#try:
#    _title = sys.argv[1]
#    _offset = sys.argv[2]
#except IndexError:
#    print 'usage: python linkedinpeoplesearch.py <keyword> <offset>'
#    sys.exit()
    
url = "http://api.linkedin.com/v1/companies/{id}/products:(id,name,type,creation-timestamp,logo-url,description,features,video:(title,url),product-deal:(title,url,text),sales-persons,num-recommendations,recommendations:(recommender,id,product-id,text,reply,timestamp,likes:(timestamp,person)),product-category,website-url,disclaimer)&format=json"

consumer = oauth.Consumer(
     key = linkedincredentials.CONSUMER_KEY,
     secret = linkedincredentials.CONSUMER_SECRET)
     
token = oauth.Token(
     key = linkedincredentials.USER_TOKEN, 
     secret = linkedincredentials.USER_SECRET)

client = oauth.Client(consumer, token)

resp, content = client.request(url)
#print resp
print content

#resp, content = client.request(url)

items = json.loads(content)
#print items
#amount = int(items['numResults'])
#print 'aantal: ' + str(amount)
#if amount < 200:
#	print 'minder dan 200'
#else:
#	print 'meer dan 200'
#entity = []
#	#print items
#for item in items['updates']['values']:
#    print 'timestamp: ' + item['timestamp']
#    print 'updatetype: ' + item['updateType']
#    try:
#        print item['updateContent']['person']['currentShare']['comment'].encode('utf-8')
#    except KeyError:
#        print 'no status'
#    try:
#        print 'voornaam: ' + item['updateContent']['person']['firstName']
#        print 'achternaam: ' + item['updateContent']['person']['lastName']
#        print 'headline: ' + item['updateContent']['person']['headline']
#    except KeyError:
#        print ''
#    try:
#        print 'url: ' + item['updateContent']['person']['apiStandardProfileRequest']['url']
#    except KeyError:
#        print 'geen url informatie'
