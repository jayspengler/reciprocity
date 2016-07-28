"""The web scraper"""

from bs4 import BeautifulSoup
import urllib2


URL = urllib2.urlopen('http://allrecipes.com/recipe/213211/turkey-and-quinoa-meatloaf/')
soup = BeautifulSoup(URL, "html.parser")

"""get the ingredients"""
#ingredients=soup.find_all(itemprop="ingredients")[1].get_text()

for item in soup.find_all(itemprop="ingredients"):
	print item.text

"""soupify it all together and display results"""

"""for i in ingredients:
	print i
"""