#!/usr/bin/python

import sys

def countword(worddict,word):


def trainmodel(filename):
   fo = open(filename)
   wordcount={}
   contextcount={}
   totalcount=0
   for line in fo:
       line = line.strip('\n')
       wordlist = line.split(' ')
       wordlist.append('</s>')
       word_f = '<s>'
       for word in wordlist:
           if(wordcount.has_key(word)==True):
               wordcount[word]+=1
           else:
               wordcount[word]=1
           #
           wordgram = word_f+' '+word
           if(contextcount.has_ky(wordgram)==True):
               contextcount[wordgram]+=1
           else:
               contextcount[wordgram]=1
   
   
   for word,value in wordcount.iteritems():
       if(totalcount==0):
           break
       wordcount[word]=(float)(wordcount[word])/totalcount
       print word,wordcount[word]


if __name__=="__main__":
    trainmodel(sys.argv[1])

def 


