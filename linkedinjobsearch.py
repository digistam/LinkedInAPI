#!/usr/bin/env python
# -*- coding: utf-8 -*-
# © 2014, Mark Stam 
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

#try:
#    _title = sys.argv[1]
#    _offset = sys.argv[2]
#except IndexError:
#    print 'usage: python linkedinpeoplesearch.py <keyword> <offset>'
#    sys.exit()

## Hacker Summary
# https://api.linkedin.com/v1/job-search:(
#  jobs:(
#    id,customer-job-code,active,posting-date,expiration-date,posting-timestamp,expiration-timestamp,company:(
#      id,name),
#    position:(
#      title,location,job-functions,industries,job-type,experience-level),
#    skills-and-experience,description-snippet,description,salary,job-poster:(
#      id,first-name,last-name,headline),
#    referral-bonus,site-job-url,location-description
#    ))
#    ?distance=10
#    &job-title=product
#    &facets=company,location
#    &facet=industry,6
#    &facet=company,1288
#    &sort=DA
    
url = "http://api.linkedin.com/v1/job-search:(jobs,facets)?keywords=sme&format=json"

consumer = oauth.Consumer(key = linkedincredentials.CONSUMER_KEY,secret = linkedincredentials.CONSUMER_SECRET)
     
token = oauth.Token(key = linkedincredentials.USER_TOKEN,secret = linkedincredentials.USER_SECRET)

client = oauth.Client(consumer, token)

resp, content = client.request(url)
#print resp
#print content

#resp, content = client.request(url)

items = json.loads(content)
print items
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
