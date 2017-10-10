#!/usr/bin/python

import sys
def trainmodel(filename):
   fo = open(filename)
   wordcount={}
   totalcount=0
   for line in fo:
       line = line.strip('\n')+' </s>'
       wordlist = line.split(' ')
       for word in wordlist:
           totalcount+=1
           if(wordcount.has_key(word)==True):
                wordcount[word]+=1
           else:
                wordcount[word]=1
   for word,value in wordcount.iteritems():
       if(totalcount==0):
           break
       wordcount[word]=(float)(wordcount[word])/totalcount
       print word,wordcount[word]


if __name__=="__main__":
    trainmodel(sys.argv[1])

