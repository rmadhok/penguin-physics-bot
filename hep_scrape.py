from bs4 import BeautifulSoup
import os
import urllib 
from unidecode import unidecode


def Soupify(url):
	html = urllib.urlopen(url).read()
	mysoup = BeautifulSoup(html, 'html.parser')
	return mysoup

# Set parameters
dir = '/Users/rmadhok/Documents/Python/twitterbot'
top = 'http://arxiv.org/'

# initiate list to hold article titles
titles = []

# In each year, follow links and scrape pages
for year in range(10,17):
	print "Getting articles from " + str(2000+year)
	url = top + '/year/hep-th/' + str(year)
	soup = Soupify(url)

	# Number of links to follow
	pages = len(soup.find('div', {'id':'content'}).findAll('li'))

	# Identify titles and add to list
	for i in range(1, pages+1):
		next_url = top + '/list/hep-th/' + str(year*100+i)
		soup = Soupify(next_url)
		divs = soup.findAll('div', {'class': 'list-title'})
		for div in divs:
			title = unidecode(div.text[8:])
			titles.append(title)


# Write titles to .txt line-by-line
os.chdir(dir)
file = open('articles.txt', 'w')
for item in titles:
  file.write("%s" % item)




