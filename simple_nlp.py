#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:46:15 2019

@author: adhamlin

What are the most frequent words and
how often do they occur?
"""
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# load data
filename = 'guidetohealth_gandhi.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

# split into words
tokens = word_tokenize(text)
# convert to lower case
tokens = [w.lower() for w in tokens]
# remove punctuation from each word
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]
# remove remaining tokens that are not alphabetic
words = [word for word in stripped if word.isalpha()]
# filter out stop words
stop_words = set(stopwords.words('english'))
words = [w for w in words if w not in stop_words]

freqdist1 = nltk.FreqDist(words)
freqdist1.plot(25)
