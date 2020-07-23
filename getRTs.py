import tweepy
import os
import urllib.request
import random
from apiSecrets import *

def authenticateTwitter():
    

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)


    api = tweepy.API(auth)
    return api

def fetchTweetURL():
    api = authenticateTwitter()
    tweets = []
    for i in range(20):
        current_tweet = api.user_timeline("papayathe2nd", tweet_mode="extended")[i]
        if "retweeted_status" in current_tweet.__dict__["_json"]:
            tweets.append(current_tweet)
   

    media_urls = []
    
    for tweet in tweets:
        try:
           
            media_urls.append(tweet.__dict__["_json"]["extended_entities"]["media"][0]["video_info"]["variants"][2]["url"])
            
        except:
            try:
                media_urls.append(tweet.__dict__["_json"]["extended_entities"]["media"][0]["media_url"])
            except KeyError as e:
                print("not an image or a video")
            
            
        else:
            next
    print(media_urls)
    return media_urls

   


def saveTweet():
    media_urls = fetchTweetURL()
    mediaPaths = []
   
    for media_url in media_urls:
        randomAppendage = ""
        for i in range(random.randint(0,11)):
            randomAppendage += str(random.randint(0, 11))
        if media_url.endswith(".mp4?tag=10"):
            urllib.request.urlretrieve(media_url, "tempMeme" + randomAppendage + ".mp4")
            mediaPaths.append("tempMeme" + randomAppendage + ".mp4")
        elif media_url.endswith(".png?tag=10") or media_url.endswith(".jpg?tag=10"):
            urllib.request.urlretrieve(media_url, "tempMeme" + randomAppendage + ".png")
            mediaPaths.append("tempMeme" + randomAppendage + ".png")
        

    return mediaPaths




