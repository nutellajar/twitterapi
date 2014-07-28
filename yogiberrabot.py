#!/usr/bin/env python

"""
A Yogi Berra Bot on Twitter. @yogicongrats
This bot will randomly query twitter for terms like 
'meaning of life', 'time for change', 'mistakes', 'pitchers'
and reply with famous Yogi Berra quotes like
'if there's a fork in the road, take it'

"""
__author__ = 'ddomingo@gmail.com'

import sys
import tweepy
from random import randint

reload(sys)
sys.setdefaultencoding('utf8')

# @yogicongrats keys and tokens
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

def main():
    query_set = ['strikeout','homerun','come from behind', 'playing baseball', 'happening again', 'pitching', 'lost', 'observation', 'challenges ahead', 'practice theory', 'rising cost of living']
    quotes_dict = {'strikeout':"Baseball is 90 percent mental and the other half is physical",'homerun':"Baseball is 90 percent mental and the other half is physical", 'come from behind':"It ain't over 'till it's over.", 'playing baseball':'Baseball is 90 percent mental and the other half is physical', 'happening again':"It's deja vu all over again", 'pitching':'All pitchers are liars or crybabies', 'lost':"You've got to be very careful if you don't know where you are going because you might not get there", 'observation':"You can observe a lot just by watching.", 'challenges ahead':'When you come to a fork in the road, take it.', 'practice theory':"In theory there's no difference between theory and practice. In practice, there is", 'rising cost of living':"A nickel ain't worth a dime anymore"}
    randomquery = query_set[randint(0,10)]
    print randomquery , quotes_dict[randomquery]
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    
    twts = api.search(q=randomquery)
    
    for t in twts:
        if not t.entities["urls"]: # only reply to tweets that don't include urls
            sn = t.user.screen_name #get the username
            m = "@%s %s #yogisms " % (sn, quotes_dict[randomquery]) #print out the reply to message here
            t = api.update_status(m, t.id) #update status
        
        

if __name__ == "__main__":
  main()
