from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import traceback
import tweepy,json,datetime,time
import pandas as pd
from pandas.core.frame import DataFrame

from bson.objectid import ObjectId

ACCESS_TOKEN = "1049234891295154177-hBsHomvCA14lS1ok9dXSMdU94AKaKh"
ACCESS_TOKEN_SECRET = "ybLLNYfNUwFrGN2clkm3zIq1jZ6kGnGGbIDfX22PGfsPU"
CONSUMER_KEY = "Xxl3PgCUjPPWCxOhIa2UE0lmT"
CONSUMER_SECRET = "8cxNBTgsjAFtQamMxwL5PMEsoiZlgfdN2JvXAjze9dAu4f5G7Q"

#Use HashTag to filter streaming Twitter
class TwitterStreamerHashTag():
    def __init__(self):
        pass
    def stream_tweets(self, fetched_tweets_filename_HashTag, hash_tag_list):
        listener = StdOutListener(fetched_tweets_filename_HashTag)
        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)

        # This filter Twitter Streams to capture data by hashtges: 
        stream.filter(track=hash_tag_list)
        return data


#Use Geo-Location to filter streaming Twitter
class TwitterStreamerGeo():
    def __init__(self):
        pass
    def stream_tweets(self, fetched_tweets_filename_Geo, geo_location):
        listener = StdOutListener(fetched_tweets_filename_Geo)
        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)
        
        # This filter Twitter Streams to capture data by geolocation: 
        stream.filter(locations=geo_location)
        return data

#Set up the Listener which is used to streaming Twitter
class StdOutListener(StreamListener):
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename
        num = 0

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    
    fetched_tweets_filename_HashTag = "tweets_HashTag.txt"
    fetched_tweets_filename_Geo_Glasgow = "tweets_Geo_Glasgow.txt"
    fetched_tweets_filename_Geo = "tweets_Geo.txt"
    fetched_tweets_filename_Raw = "tweets_Raw.txt"
    

###Streaming geo-tagged data###
#    geo_location = [-180,-90,180,90]
#    twitter_streamer = TwitterStreamerGeo()
#    twitter_streamer.stream_tweets(fetched_tweets_filename_Geo, geo_location)

###Streaming data that is from Glasgow###   
#    geo_location = [-6.38,49.87,1.77,55.81]
#    twitter_streamer = TwitterStreamerGeo()
#    twitter_streamer.stream_tweets(fetched_tweets_filename_Geo_Glasgow, geo_location)

###Streaming data using streamer and hashtags###
#    hash_tag_list = ["dota", "league of legends", "esports", "overwatch"]
#    twitter_streamer = TwitterStreamerHashTag()
#    twitter_streamer.stream_tweets(fetched_tweets_filename_HashTag, hash_tag_list)

###Streaming geo-tagged data###
#    geo_location = [-180,-90,180,90]
#    twitter_streamer = TwitterStreamerGeo()
#    twitter_streamer.stream_tweets(fetched_tweets_filename_Geo, geo_location)


    

    


