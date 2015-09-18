'''
Created on 2015-9-8

@author: ytl
'''

# -*- coding:utf-8 -*-

import os
print os.system('pwd')

import urllib
import urllib2
import re

root=u'https://en.wikipedia.org/wiki/'
url=u'https://en.wikipedia.org/wiki/Lists_of_prepared_foods'
response  = urllib2.urlopen(url)
result= response.read()
result = result.decode('UTF-8')

page = re.findall(r'<li><a\s*href\s*=\s*"(/wiki/List[^"]*)"\s*title', result)
LEN=len(page)
#LEN=3
print 'len: %s' % len(page)

id={}
foodUrl={}  #-> link
foodName={} 
foodName2={} #-> title
foodPage={}
foodPicsUrl={}
foodDiscript={} #-> summary
foodDict={}  #->keys
foodLess={} #->summaryLess

#get info
import codecs
import os.path

#prepare for nessary message        
for i in range(LEN):
    id[page[i]]=i
    foodName[i]=re.match(r'^.*List_of_(.*)$', page[i]).group(1)
    foodName2[i]=foodName[i].replace('_',' ')
    #foodUrl[i]=root+re.match(r'^.*(List_of_.*)$',page[i]).group(1)
    #foodPicsUrl[i]= re.findall(r'src="//(upload.*jpg)"',foodPage[i])
    print 'get %s' % foodName2[i]

	
# load	
import json
for i in range(LEN):
	# store html
	dir = 'spider/resource/%s/%s.html' % (foodName[i],foodName[i])
	file=codecs.open(dir,'r','utf-8');
	str=file.read()
	file.close()
	foodPage[i]=json.loads(str)
	
	# store summary
	dir='spider/resource/%s/summary.txt' % (foodName[i])
	file=codecs.open(dir,'r','utf-8');
	str  =file.read()
	file.close()
	foodDiscript[i]=json.loads(str)
	
	# store link
	dir='spider/resource/%s/url.txt' % (foodName[i])
	file=codecs.open(dir,'r','utf-8');
	str = file.read()
	file.close()
	foodUrl[i] = json.loads(str)
	
	# store title	
	dir='spider/resource/%s/name.txt' % (foodName[i])
	file=codecs.open(dir,'r','utf-8');
	str = file.read()
	file.close()
	foodName2[i]  = json.loads(str)
	
	# store keys
	dir='spider/resource/%s/keys.txt' % (foodName[i])
	file=codecs.open(dir,'r','utf-8');
	str = file.read()
	file.close()
	foodDict[i] = json.loads(str)

	foodLess[i]=foodDiscript[i][0:300]
	
	print 'load %s' % foodName[i]

print 'complete'