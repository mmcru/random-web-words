__author__ = 'crupi'

import urllib3
import re
from random import randint


def getrandoms (webpage, numwords, length):

    #print("choosing %s word(s) from %s with length over %s characters..." % (numwords, webpage, length))

    #print("fetching and decoding raw html...")
    http = urllib3.PoolManager()
    get = http.request('GET', webpage)
    rawhtml = get.data.decode("utf-8")

    #print("filtering out punctuation and other non-english characters...")
    step1 = re.sub("\\W|\\d|_|page", " ", rawhtml)
    step2 = re.sub("[ ]*[ ]", " ", step1)
    totalwords = step2.lower().split(" ")

    #print("subtracting words with length under %s..." % length)
    filtered = [i for i in totalwords if len(i) >= length]

    #this removes duplicate values
    #print("removing duplicate values...")
    setit = set(filtered)
    backtolist = list(setit)

    #print("found %s words on %s" % (len(backtolist), webpage))
    #print('choosing %s random words from selection...' % numwords)
    finallist = []
    i = 0
    while True:
        randomforlist = randint(0,(len(backtolist)) - 1)
        finallist += [backtolist[randomforlist]]
        i += 1
        if i >= numwords:
            break

    return finallist
