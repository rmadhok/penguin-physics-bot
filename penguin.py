#to do
# CLEAN UP SCRIPT
# ADAPT MORE
# BETTER IF/ELSE
# FIGURE OUT BASH AND SYS.ARGV
# CRON JOB


import sys
import random
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import tweepy
import json
import os

dir = '/Users/rmadhok/Documents/Python/twitterbot'
os.chdir(dir)

#Authentification
with open('secrets.json') as keys:
	SECRETS = json.load(keys)
#Input secrets
CONSUMER_KEY = SECRETS['consumer_key']
CONSUMER_SECRET = SECRETS['consumer_secret']
ACCESS_TOKEN = SECRETS['access_token']
ACCESS_SECRET = SECRETS['access_secret']

#Initiate API Interaction
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

#TEST - read markov text
file = open('jumble.txt', 'r')
sentence = file.readline()

#Choose word limit between 60-135 characters
#Remove last word incase cut off
if len(sentence)-1 > 130:
    print "truncating sentence to fit twitter character limit..."
    word_limit = random.randint(60,135)
    sentence = sentence[0:word_limit].split(" ")
    sentence = sentence[0:len(sentence)-1]
    sentence = ' '.join(sentence)

#Tokenize and check grammar
tokens = word_tokenize(sentence)
pos = pos_tag(tokens)

#Array to add nouns/adjectives
nouns = []
adjectives = []


for word in pos:
	# Check for nouns
    if word[1] == "NN" or word[1] == "NNP" or word[1] == "NNS":
        nouns.append(word)
    #Check for adjectives
    if word[1] == "JJ":
        adjectives.append(word)


rand = random.randint(0,len(nouns)-1)

#IMPROVE THIS IF ELSE 
penguin = "Penguin"
if rand == 0:
    penguin = "Penguin"

if nouns[rand][1] == "NNS":
    penguin = "Penguin"

#Set sentence
penguinsentence = sentence.replace(nouns[rand][0],penguin,1)

print penguinsentence

#If there are adjectives, randomly select one
if len(adjectives) > 0:
    duck = adjectives[random.randint(0,len(adjectives)-1)][0]
#Replace in long sentences
if len(penguinsentence) > 100:
    penguinsentence = penguinsentence.replace(duck, "Duck")

#Post to Twitter
api.update_status(penguinsentence)