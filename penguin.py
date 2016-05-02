import sys
import random
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import tweepy
import json

with open('secrets.json') as keys:
	SECRETS = json.load(keys)

CONSUMER_KEY = SECRETS['consumer_key']
CONSUMER_SECRET = SECRETS['consumer_secret']
ACCESS_TOKEN = SECRETS['access_token']
ACCESS_SECRET = SECRETS['access_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)