from wordcloud import WordCloud
import matplotlib.pyplot as plt

from os import path
import numpy as np
from PIL import Image

class MaskCloud(object):
	def __init__(self, text):
		self.text = text

	def generate_cloud(self, image_name, image_out_name, max_font=50, scaling=.5):
		d = path.dirname(__file__)
		image = np.array(Image.open(path.join(d, image_name)))
		# take relative word frequencies into account, lower max_font_size
		print 'Generating word cloud image...'
		wordcloud = WordCloud(background_color="white", max_words=2000, mask=image).generate(self.text)

		d = path.dirname(__file__)
		wordcloud.to_file(path.join(d, image_out_name))