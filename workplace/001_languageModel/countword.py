#!/usr/bin/python
import sys

def countword(filename):
   fo = open(filename,"r");
   countmap = {}
   for line in fo:
       words = line.strip('\n').split(' ')
       for word in words:
           if(countmap.has_key(word)==True):
               countmap[word]=countmap[word]+1
           else:
               countmap[word]=1
   for key,value in countmap.iteritems():
       print key,value




if __name__=="__main__":
    countword(sys.argv[1])

   

