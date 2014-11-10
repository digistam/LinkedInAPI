import oauth2 as oauth
import time
from time import sleep
import datetime
now = datetime.datetime.now()
from time import sleep
import linkedincredentials
import sys
import urllib2
import json

keyword = "AGT"
url = "http://api.linkedin.com/v1/company-search?keywords={0}&format=json" .format(keyword)

consumer = oauth.Consumer(key = linkedincredentials.CONSUMER_KEY,secret = linkedincredentials.CONSUMER_SECRET)
     
token = oauth.Token(key = linkedincredentials.USER_TOKEN,secret = linkedincredentials.USER_SECRET)

client = oauth.Client(consumer, token)

resp, content = client.request(url)
#print content

items = json.loads(content)
total = items['companies']['_total']
print 'het totaal aantal: ' + str(total)
offset = 0
while offset < int(total) + 1:
    nexturl = "http://api.linkedin.com/v1/company-search:(companies:(id,name,universal-name,website-url,industries,status,logo-url,blog-rss-url,twitter-id,employee-count-range,specialties,locations,description,stock-exchange,founded-year,end-year,num-followers))?keywords={0}&start=" + str(offset) + "&count=25&format=json" .format(keyword)
    resp, nextcontent = client.request(nexturl)
    items = json.loads(nextcontent)
    entity = []
    for item in items['companies']['values']:
        entity.append(item)
    for i in range(len(entity)):
        print entity[i]['id']
        print entity[i]['name'].encode('utf-8')
        try:
            print entity[i]['industries']
        except KeyError:
            print 'no industries'
        try:
            print entity[i]['numFollowers']
        except KeyError:
            print 'no followers'
        try:
            print entity[i]['description'].encode('utf-8')
        except KeyError:
            print 'no description'
        try:
            print entity[i]['twitterId']
        except KeyError:
            print 'no twitterId'
        try:
            print entity[i]['locations']
        except KeyError:
            print 'no locations'
        try:
            print entity[i]['employeeCountRange']
        except KeyError:
            print 'no employee count details'
        try:
            print entity[i]['foundedYear']
        except KeyError:
            print 'no foundedYear'
        try:
            print entity[i]['websiteUrl']
        except KeyError:
            print 'no websiteurl'
        try:
            print entity[i]['specialties']
        except KeyError:
            print 'no specialties'
        try:
            print entity[i]['status']
        except KeyError:
            print 'no status'
        try:
            print entity[i]['logoUrl']
        except KeyError:
            print 'no logoUrl'
        print entity[i]['universalName']
        print '-----------------'
    offset += 25
    print 'de offset is: ' + str(offset)
    sleep(5)
    
