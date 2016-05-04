import sys
import random
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import tweepy
import json
import os

#dir = '/Users/rmadhok/Documents/Python/twitterbot'
#os.chdir(dir)

### 1. Set up API Connection
# Extract Keys and Tokens
with open('secrets.json') as keys:
	SECRETS = json.load(keys)

CONSUMER_KEY    =  SECRETS['consumer_key']
CONSUMER_SECRET =  SECRETS['consumer_secret']
ACCESS_TOKEN    =  SECRETS['access_token']
ACCESS_SECRET   =  SECRETS['access_secret']

# Authenticate 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

### 2. Assemble Tweets
file = open(sys.argv[1], "r")
sentence = file.readline()

#2a. Set Tweet word limit
if len(sentence) > 130:
    print "Truncating to fit character limit..."
    # Randomly choose short/long limit
    word_limit = random.randint(60,130)
    # Remove last word in case it gets cut off
    sentence   = sentence[0:word_limit].split(" ")
    sentence   = sentence[0:len(sentence)-1]
    badwords = ['if', 'in', 'when', 'the', 'and', 'when', 
                'where', 'of', 'for', 'a', 'with']
    if sentence[:-1] in badwords:
        sentence = sentence[len(sentence)-1]
    sentence   = ' '.join(sentence)

#2b. Tag part-of-speech from trained NLTK model
tokens = word_tokenize(sentence)
pos = pos_tag(tokens)
nouns = []
adjectives = []

for word in pos:
	# Check for nouns (singular, plural, or proper)
    if word[1] == "NN" or word[1] == "NNP" or word[1] == "NNS":
        nouns.append(word)
    #Check for adjectives
    if word[1] == "JJ":
        adjectives.append(word)

#2c. Insert Penguin into Noun
# Replace 'Penguin' into random index
rand = random.randint(0,len(nouns)-1)
if rand == 0:
    penguin = "Penguin"     # Capitalize if first word
elif nouns[rand][1] == "NNS":
    penguin =  "penguins"   # Pluralize if replacing plural noun
else:
    penguin = "penguin"
print "Inserting penguin..."
penguinsentence = sentence.replace(nouns[rand][0],penguin,1)


#2d. Select Adjective to replace
if len(adjectives) > 0:
    duck = adjectives[random.randint(0,len(adjectives)-1)][0]
# Replace in longer sentences
    if len(penguinsentence) > 100:
        print "Inserting duck..."
        penguinsentence = penguinsentence.replace(duck, "duck")

#Post to Twitter
print "Posting to Twitter..."
api.update_status(penguinsentence)