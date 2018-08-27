# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 19:48:09 2018

@author: dadangewp
"""

import codecs
import re
from nltk.stem.porter import PorterStemmer
import os

class LIWCCogmech(object):

    liwccogmech=[]

    def __init__(self):
        self.liwccogmech = []
        dirname = os.path.dirname(__file__)
        stemmer = PorterStemmer()
        #http://www2.imm.dtu.dk/pubdb/views/publication_details.php?id=6010
        file=codecs.open(dirname + '//resources//LIWC-COGMECH.txt', encoding='UTF-8')
        for line in file:
            word = line.strip("\r\n")
            word = stemmer.stem(word)
            self.liwccogmech.append(word)
        #print(self.liwcpos)    
        self.pattern_split = re.compile(r"\W+")
        return

    def get_liwccogmech_sentiment(self,text):
        
        stemmer = PorterStemmer()
        counter=0
        words = self.pattern_split.split(text.lower())
        words = text.split(" ")
        #print (words)
        #print (self.liwcpos)
        for word in words:
            stemmed = stemmer.stem(word)
            #print(stemmed)
            if stemmed in self.liwccogmech:
                counter = counter + 1


        return counter


if __name__ == '__main__':
    liwccogmech = LIWCCogmech()
    sentiment=liwccogmech.get_liwccogmech_sentiment("absolutely")
    print(sentiment)