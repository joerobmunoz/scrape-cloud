#!/usr/bin/env python2

"""
Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""

from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt


class Cloud(object):
	def __init__(self, text):
		self.text = text

	def generate_cloud(self, max_font=50, scaling=.5):
		# take relative word frequencies into account, lower max_font_size
		print 'Generating word cloud image...'
		wordcloud = WordCloud(max_font_size=max_font, relative_scaling=scaling).generate(self.text)
		plt.figure()
		plt.imshow(wordcloud)
		plt.axis("off")
		plt.show()