#!/usr/bin/env python
# -*- coding: utf-8 -*-
# © 2014, Mark Stam 
import oauth2 as oauth
import time
from time import sleep
import datetime
from datetime import datetime
from time import strftime
import linkedincredentials
import sys
import json

url = "http://api.linkedin.com/v1/people/~/network/updates:(update-content:(person:(firstName,lastName,headline,site-standard-profile-request,currentShare)))?type=SHAR&format=json"

consumer = oauth.Consumer(key = linkedincredentials.CONSUMER_KEY,secret = linkedincredentials.CONSUMER_SECRET)
     
token = oauth.Token(key = linkedincredentials.USER_TOKEN,secret = linkedincredentials.USER_SECRET)

client = oauth.Client(consumer, token)

resp, content = client.request(url)

items = json.loads(content)
total = items['_total']
print 'het totaal aantal: ' + str(total)
offset = 0
while offset < int(total) + 1:
    nexturl = "http://api.linkedin.com/v1/people/~/network/updates:(update-content:(person:(firstName,lastName,headline,site-standard-profile-request,currentShare)))?type=SHAR&count=25&start=" + str(offset) + "&format=json"
    resp, nextcontent = client.request(nexturl)
    items = json.loads(nextcontent)
    entity = []
    for item in items['values']:
        try:
            print 'timestamp: ' + str(item['updateContent']['person']['currentShare']['timestamp'])
        except KeyError:
            print 'niets'
        try:
            print item['updateContent']['person']['currentShare']['comment'].encode('utf-8')
        except KeyError:
            print 'no status'
        try:
            print 'voornaam: ' + item['updateContent']['person']['firstName'].encode('utf-8')
            print 'achternaam: ' + item['updateContent']['person']['lastName'].encode('utf-8')
            print 'headline: ' + item['updateContent']['person']['headline'].encode('utf-8')
        except KeyError:
            print ''
        try:
            print 'url: ' + item['updateContent']['person']['siteStandardProfileRequest']['url'].encode('utf-8')
        except KeyError:
            print 'geen url informatie'
        print '----------------'
    offset += 25
    print 'de offset is: ' + str(offset)
    sleep(5)
