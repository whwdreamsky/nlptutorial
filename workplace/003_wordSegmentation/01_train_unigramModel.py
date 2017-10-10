#!/usr/bin/python

import sys
def trainmodel(filename):
   fo = open(filename)
   wordcount={}
   totalcount=0
   for line in fo:
       line = unicode(line,"utf-8")
       line = line.strip('\n')+unicode(' </s>','utf-8')
       wordlist = line.split()
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
       print word.encode('utf-8'),wordcount[word]


if __name__=="__main__":
    trainmodel(sys.argv[1])

