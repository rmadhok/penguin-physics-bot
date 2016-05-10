### TwitterBot

A twitterbot I made based on this [markov text generator](https://github.com/codebox/markov-text). 
See (and follow) the final twitter page [here](www.twitter.com/penguinphysics1).

#### Description
* First, I scrape thousands of titles from a database of physics journals into a text file. I know nothing about high energy particle physics, I just needed base text for the tweets. 
* Second, I run the markov text generator on the text file which spits out a logical-but-incoherent sentence.
* I limit the character count, tag the grammar with the NLTK machine learning library, and replace a noun with "penguin". Sometimes a duck enters when the sentence is long enough and there are adjectives.
* Post to twitter via the API
* Example of latest tweet: Gravitational instantons constraining de penguin: a codimension-2 brane

note: The scripts are running in a cron job -- a tweet is posted every morning

#### Resources
* [Twitterbot tutorial](http://www.dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/)
* [Twitterbot wiki](https://botwiki.org/tutorials/twitterbots/)
* [Cronjob examples](http://www.thegeekstuff.com/2009/06/15-practical-crontab-examples/)
