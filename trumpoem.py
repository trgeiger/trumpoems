#!/usr/bin/python

from sys import argv
from random import randint
import string


# organize command line arguments
num_args = len(argv)
poem_words = int(argv[1])

# open, split, and lowercase the transcript
text = open("transcript.txt").read().lower().split()

# remove punctuation from edges of each word
text = [word.strip(string.punctuation) for word in text]

# should be 1450 words
word_count = len(text)
poem_list = []

# assemble the poem word list
for word in range(poem_words):
    poem_list.append(text[randint(0, word_count)])

# replace awkward ending words
while poem_list[-1] in ['and', 'an', 'the', 'to', 'but', 'in', 'their']:
    poem_list.pop()
    poem_list.append(text[randint(0, word_count)])

# replace sequentially repeated words
for i in range(poem_words-1):
    if poem_list[i] == poem_list[i+1]:
        poem_list[i+1] = text[randint(0, word_count)]


print(" ".join(poem_list))
