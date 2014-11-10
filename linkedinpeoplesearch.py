#!/usr/bin/env python
# -*- coding: utf-8 -*-
# © 2014, Mark Stam 
import oauth2 as oauth
import time
from time import sleep
import linkedincredentials
import sys
import json

## Hacker Summary:
# https://api.linkedin.com/v1/people-search
#   ?keywords=[space delimited keywords]
#   &first-name=[first name]
#   &last-name=[last name]
#   &company-name=[company name]
#   &current-company=[true|false]
#   &title=[title]
#   &current-title=[true|false]
#   &school-name=[school name]
#   &current-school=[true|false]
#   &country-code=[country code]
#   &postal-code=[postal code]
#   &distance=[miles]
#   &start=[number]
#   &count=[1-25]
#   &facet=[facet code, values]
#   &facets=[facet codes]
#   &sort=[connections|recommenders|distance|relevance]

keyword = "pianist"
url = "http://api.linkedin.com/v1/people-search:(people:(id,first-name,last-name,picture-url,headline,public-profile-url,last-modified-timestamp,positions:(company:(name,id)),location:(name,country:(code)),distance),num-results)?keywords={0}&format=json" .format(keyword)

consumer = oauth.Consumer(
     key = linkedincredentials.CONSUMER_KEY,
     secret = linkedincredentials.CONSUMER_SECRET)
     
token = oauth.Token(
     key = linkedincredentials.USER_TOKEN, 
     secret = linkedincredentials.USER_SECRET)

client = oauth.Client(consumer, token)

resp, content = client.request(url)

items = json.loads(content)
amount = int(items['numResults'])
print 'aantal: ' + str(amount)

entity = []

offset = 0
while offset < int(amount) + 1:
    nexturl = "http://api.linkedin.com/v1/people-search:(people:(id,first-name,last-name,picture-url,headline,public-profile-url,last-modified-timestamp,positions:(company:(name,id)),location:(name,country:(code)),distance),num-results)?count=25&start=" + str(offset) + "&keywords={0}&format=json" .format(keyword)
    resp, nextcontent = client.request(nexturl)
    items = json.loads(nextcontent)
    entity = []
  
    for item in items['people']['values']:
        print 'id: ' + item['id']
        print 'first name: ' + item['firstName'].encode('utf-8')
        print 'last name: ' + item['lastName'].encode('utf-8')
        try:
            print 'headline: ' + item['headline'].encode('utf-8')
        except KeyError:
            print 'no headline'
#	try:
#		print 'picture: ' + entity[i]['pictureUrl']
#	except KeyError:
#		print 'no picture'
#	try:
#		print 'last modified: ' + entity[i]['last-modified-timestamp']
#	except KeyError:
#		print 'no last modification details'
#	try:
#		print 'location: ' + entity[i]['location']['name']
#	except KeyError:
#		print 'no location'
#	try:
#		print 'country: ' + entity[i]['location']['country']['code']
#	except KeyError:
#		print 'no country details'
#	try:
#		print 'company: ' + entity[i]['positions']['values'][0]['company']['name']
#	except KeyError:
#		print 'no company'
#	try:
#		print 'distance: ' + str(entity[i]['distance'])
#	except KeyError:
#		print 'no distance'
#	try:
#		print 'public profile: ' + entity[i]['publicProfileUrl']
#	except KeyError:
#		print 'no public profile'
#	print entity[i]['numFollowers']
#	try:
#		print entity[i]['status']
#	except KeyError:
#		print 'no status'
    offset += 25
    print 'de offset is: ' + str(offset)
    sleep(5)
