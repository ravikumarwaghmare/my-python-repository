
import pandas as pd
import tweepy
import csv
from textblob import TextBlob
import time



class TwitterClient(object):
    '''
    Access twitter
    '''
    def __init__(self):
    ##Twitter keys --These are dummy tokens and keys
        consumer_key = '5Xyd22lkdslkdssdsdsd'
        consumer_secret = 'TIj4iEJuYlVZhvPRIaaaaSIVRQtVokie3453klsdFbk5FE'
        access_token = '333liosd-WrUzObAoKXVsdsd98928303xNj8YFGVWk5vn'
        access_token_secret = '2222JEXRhasdaXxf7o7sd9S7FsdGIzKqwqw222'
        ###Try logging

        try:
            ####Handler objects
            self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            ####Set access token and secrets
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
            
            print("Connection successful")

        except:
            print("Error : Authentication failed")
        




    def get_tweets(self):
        csvFile = open('download.csv', 'a')
        csvWriter = csv.writer(csvFile)
        for tweet in tweepy.Cursor(self.api.search, q="#rkwrkwrkwrkwrkw",count=100,lang="en",since="2018-07-15").items():
             ###    print (tweet.created_at, tweet.text)
             csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])



####Connect to twitter 

# creating object of TwitterClient Class
api = TwitterClient()
tweets = api.get_tweets()

