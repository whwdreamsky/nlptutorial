#!/usr/bin/python
#coding=utf-8
import sys
import math


def testmodel(modelfile,testfile):
    fo = open(modelfile)
    ftest =open(testfile)
    pword={}
    testword=0
    namda = 0.95
    pse =0.0
    V = 10000
    unk=0
    H=0.0
    for line in fo:
        tmp = line.strip('\n').split(' ')
        pword[tmp[0]]=(float)(tmp[1])
    for line in ftest:
        line = line.strip('\n')+' </s>'
        wordlist = line.split(' ')
        for word in wordlist:
            testword+=1
            pse = (1-namda)/V
            if(pword.has_key(word)==True):
                pse=pse+namda*(pword[word])
            else:
                #why p of unk don't count
                unk+=1
            H+=-1*math.log(pse,2)
            print 'h:',math.log(pse,2)
        #计算每个句子概率的平均值
    if testword!=0:
        H=H/testword
    print "entropy = ",H
    print "coverage = ",(float)(testword-unk)/testword





if __name__=="__main__":
    testmodel(sys.argv[1],sys.argv[2])


