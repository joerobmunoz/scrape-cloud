from os import path
from bs4 import BeautifulSoup
import urllib2
from cloud import Cloud


visible_text = ''
urls = ['https://github.com/amueller/word_cloud']

for i, url in enumerate(urls):
	print 'Fetching url contents %s of %s' % (str(i+1), str(len(urls)))
	html = urllib2.urlopen(url).read()
	soup = BeautifulSoup(html, 'html5lib')

	[s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title', 'iframe'])]
	visible_text = soup.getText().encode('utf-8', 'ignore')


cloud = Cloud(visible_text)
cloud.generate_cloud()
print '\nComplete'