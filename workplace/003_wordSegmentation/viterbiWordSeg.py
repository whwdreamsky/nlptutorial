#!/usr/bin/python
#coding = utf-8
import sys
import math
probs={}
best_edge = []
P_UNKNOWNWORD = math.pow(10,-10)
class Edge:
	def __init__(self,fromedge=0,toedge=0):
		self.fromedge = fromedge
		self.toedge = toedge

def loadModle(filename):
	f = open(filename)
	for line in f:
		line  = unicode(line,'utf-8')
		templist = line.strip('\n').split()
		if len(templist)==2:
			probs[templist[0]] = float(templist[1])

	f.close()

def forWordSeg(wordline):
	best_score=[0 for n in range(len(wordline)+1)]
	best_score[0]=0
	global best_edge
	del best_edge[:]
	for wordend in range(1,len(wordline)+1):
		#best_score[wordend] = -math.log(P_UNKNOWNWORD)
		best_score[wordend]=100000
		edgeindex =wordend-1 
		for wordbegin in range(0,wordend):
			#print wordline[wordbegin:wordend].encode('utf-8')
			if(probs.has_key(wordline[wordbegin:wordend])==True):
				#print 'found' + wordline[wordbegin:wordend].encode('utf-8')
				probsword = -math.log(probs[wordline[wordbegin:wordend]])+best_score[wordbegin]
				if(probsword<best_score[wordend]):
					best_score[wordend] = probsword
					edgeindex = wordbegin


		best_edge.append(Edge(fromedge=edgeindex,toedge=wordend))

def viterbiWordSeg(wordline):
	forWordSeg(wordline);
	wordsegresult = backwordSeg(wordline)
	return wordsegresult


def backwordSeg(wordline):
	wordsegindex=[]
	lastedge = best_edge[len(best_edge)-1]
	fromedge = lastedge.toedge
	while fromedge!=0:
		wordsegindex.append(fromedge)
		#check edge out put
		fromedge = best_edge[fromedge-1].fromedge
	wordsegindex.append(0)
	wordsegindex.reverse()
	index = wordsegindex[0]
	wordsegresult = wordline[wordsegindex[0]:wordsegindex[1]]
	for item in range(2,len(wordsegindex)-1):
		wordsegresult = wordsegresult+' '+wordline[wordsegindex[item]:wordsegindex[item+1]]
	return wordsegresult.encode('utf-8')

def main():
	modlefile = sys.argv[1]
	trainfilename = sys.argv[2]
	loadModle(modlefile)
	ftrain = open(trainfilename)
	for line in ftrain:
		line = unicode(line,'utf-8')
		line = line.strip('\n')
		wordsegresult = viterbiWordSeg(line)
		print wordsegresult

if __name__ == '__main__':
	main()
