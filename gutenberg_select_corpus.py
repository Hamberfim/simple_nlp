#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:46:15 2019

@author: adhamlin
"""

import nltk
from nltk.corpus import gutenberg


# embeded corpus - available works as a list
corpus = nltk.corpus.gutenberg.fileids()

# iterate over list indexing/titles
for i, item in enumerate(corpus):
    print(i, item)

# user selection via numerical index
select = input("Indicate your book choice by selecting it's numeric value: ")

# cast input to integer
book = int(select)

# loop through embeded corpus matching user input selection
# print number of words and last 12 words
for num, title in enumerate(corpus):
    if book == num:
        choice = gutenberg.words(title)  # Tokenize
        print("Number of words:", len(choice))
        print()  # create space
        chain_words = choice[-12:]
        print("The title of your choice is:", title)
        print()  # create space
        print("The last line from your choice:")
        for word in chain_words:
            word = word.replace("_", "'")
            print(word, end=" ")
