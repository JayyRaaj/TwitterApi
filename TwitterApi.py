# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 09:50:47 2017

@author: iamgj
"""



import tweepy 


#consumer key, consumer secret, access token, access secret.
access_key = " ... "
access_secret = " ... "
consumer_key = "..."
consumer_secret = "..."

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api=tweepy.API(auth)
print (api.me().name)

count=0
timeline = api.user_timeline(screen_name='Twitter Handle', include_rts=False, count=900)

for tweet in timeline:
        count+=1
        print ("\n")
        print ("ID:", tweet.id)
        print ("User ID:", tweet.user.id)
        print ("Text:", tweet.text)
        print ("Created:", tweet.created_at)
        print ("Geo:", tweet.geo)
        print ("Contributors:", tweet.contributors)
        print ("Coordinates:", tweet.coordinates) 
        print ("Favorited:", tweet.favorited)
        print ("In reply to screen name:", tweet.in_reply_to_screen_name)
        print ("In reply to status ID:", tweet.in_reply_to_status_id)
        print ("In reply to status ID str:", tweet.in_reply_to_status_id_str)
        print ("In reply to user ID:", tweet.in_reply_to_user_id)
        print ("In reply to user ID str:", tweet.in_reply_to_user_id_str)
        print ("Place:", tweet.place)
        print ("Retweeted:", tweet.retweeted)
        print ("Retweet count:", tweet.retweet_count)
        print ("Source:", tweet.source)
        print ("Truncated:", tweet.truncated)
print(count)