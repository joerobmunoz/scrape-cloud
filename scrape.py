from bs4 import BeautifulSoup
import urllib2
from cloud import Cloud

class ScrapeCloud(object):
	def __init__(self, urls):
		"""
		urls: A list of string urls to scrape and generate a single word cloud image.
		"""

		self.urls = urls
		self.visible_text = ''

		for i, url in enumerate(urls):
			print 'Fetching url contents %s of %s' % (str(i+1), str(len(urls)))
			html = urllib2.urlopen(url).read()
			soup = BeautifulSoup(html, 'html5lib')

			[s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title', 'iframe'])]
			self.visible_text = soup.getText().encode('utf-8', 'ignore')


		cloud = Cloud(self.visible_text)
		cloud.generate_cloud()
		print '\nComplete'

urls = ['https://github.com/amueller/word_cloud']
ScrapeCloud(urls)
