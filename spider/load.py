'''
Created on 2015-9-8

@author: ytl
'''

# -*- coding:utf-8 -*-


import urllib
import urllib2
import re
import codecs
import os.path
import json
import copy

myindex=[]
packages=[]

rrr='spider/'
#rrr=''

ddir=rrr+'resource/list.txt'
file=codecs.open(ddir,'r','utf-8');
str = file.read()
file.close()
myindex = json.loads(str)


def myload(mydir):
	foodName={} 
	package={}
	package['name']=mydir
	package['title']={}
	package['summary']={}
	package['link']={}
	package['summaryLess']={}
	package['keys']={}
	package['linkPos']={}

	dir = rrr+'resource/%s/index.txt' % (mydir)
	file=codecs.open(dir,'r','utf-8');
	str=file.read()
	file.close()
	foodName=json.loads(str)
	
	LEN = len(foodName)
	#LEN = 3

	# load	
	for ii in range(LEN):
		i = '%d' % ii
		link={}  #-> link
		title={} #-> title
		summary={} #-> summary
		keys={}  #->keys
		summaryLess={} #->summaryLess
		
		linkPos ='/static/%s/%s/%s.html' % (mydir,foodName[i],foodName[i]) 
		# store html
		#dir = 'spider/resource/%s/%s.html' % (foodName[i],foodName[i])
		#file=codecs.open(dir,'r','utf-8');
		#str=file.read()
		#file.close()
		#foodPage[i]=json.loads(str)
		
		# store summary
		dir=rrr+'resource/%s/%s/summary.txt' % (mydir,foodName[i])
		file=codecs.open(dir,'r','utf-8');
		str  =file.read()
		file.close()
		summary=json.loads(str)
		
		# store link
		dir=rrr+'resource/%s/%s/url.txt' % (mydir,foodName[i])
		file=codecs.open(dir,'r','utf-8');
		str = file.read()
		file.close()
		link = json.loads(str)
		
		# store title	
		dir=rrr+'resource/%s/%s/name.txt' % (mydir,foodName[i])
		file=codecs.open(dir,'r','utf-8');
		str = file.read()
		file.close()
		title  = json.loads(str)
		
		# store keys
		dir=rrr+'resource/%s/%s/keys.txt' % (mydir,foodName[i])
		file=codecs.open(dir,'r','utf-8');
		str = file.read()
		file.close()
		keys = json.loads(str)	

		summaryLess=summary[0:300]
	
		package['title'][ii]=copy.deepcopy(title)
		package['summary'][ii]=copy.deepcopy(summary)
		package['summaryLess'][ii]=copy.deepcopy(summaryLess)
		package['link'][ii]=copy.deepcopy(link)
		package['keys'][ii]=copy.deepcopy(keys)
		package['linkPos'][ii]=linkPos
		#print 'keys: ',i,' ',package['keys'][i]
		package['LEN']=len(foodName)
		print 'load %s' % foodName[i]

	#print 'len:',len(package['keys'])
	#print package['keys'].keys()
	#print package['keys']['0']
	print '------- load package %s complete' % mydir
	return package


for mydir in myindex:
	package = myload(mydir)
	packages.append(package)
myindex.append('all')

print 'complete'
