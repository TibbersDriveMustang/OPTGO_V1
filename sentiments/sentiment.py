#!/usr/bin/python
#-*- coding:utf-8 -*-
from __builtin__ import *
import textblob
import requests
from pylab import *


def get_stats():
	try:
		#link = "https://raw.githubusercontent.com/shadowwalker/optgo/master/data/comments.txt"
		link = "file:///../data/comments.txt"
		f = requests.get(link)
	except:
		print 'not work'

	pos = 0
	neg = 0

	#distinct
	data = [l.strip('\n') for l in f]
	data = list(set(data))
	print "sentences:",len(data)
	for line in data:
		score = textblob.TextBlob(line).sentiment.polarity
		#for t in line.split('.'):
		#	score = textblob.TextBlob(t).sentiment.polarity
		if score > 0.7:
			pos += 1
		elif score < -0.5:
			neg += 1
			return float(pos)/(pos+neg)

def make_pie(percent):
	figure(1, figsize=(6,6))
	ax = axes([0.1, 0.1, 0.8, 0.8])

	labels = 'Positive', 'Negative'
	fracs = [100*percent, 100.-100*percent]
	explode=(0.05, 0)
	colors = ['green', 'red']

	pie(fracs, explode=explode, labels=labels,	autopct='%1.1f%%', shadow=True, startangle=90, colors = colors)

	title('OPT extension comments', bbox={'facecolor':'0.8', 'pad':5})
	savefig('./pie.png')

make_pie(get_stats())
