# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect

from spider.load import packages
from spider.load import myindex

def test(request):
	print '!!!',request,'###\n'
	return render(request,'test.html')

def index(request):
	if (request.method=='POST'):
		print request.POST
		return HttpResponse('aaaa')
	return HttpResponseRedirect('/search')
	#return render(request,'home.html')

def notfound(request):
	return render(request,'notfound.html')

def searchIndex(request):
	print 'in searchIndex'
	if request.GET.has_key('word'):
		word=request.GET.get('word')
		return search(request,word);#render(request,'search.html',{'word':word})
	else:
		return render(request,'searchindex.html',{'word':''})
	
	
def search(request,word):
	return HttpResponseRedirect('/search/all/%s/1' % (word));
	#return searchPage(request,'all',word,1)

def to_searchPage(request,word,pdId):
	return HttpResponseRedirect('/search/all/%s/%s' % (word,pdId));



def searchPage(request,where,myword,pgId):
	words=myword.split(' ')
	pageId = int(pgId)
	pages=[]
	info={};
	tot=0
	print 'where:',where 
		
	l=(pageId-1)*10+1;r=pageId*10;
	for word in words:
		print '!!! ',word

	for word in words:
		for package in packages:
			if (where == 'all') or (package['name']==where): 
				#print 'find in package:',package['name']
				ttt=0
				for i in range(package['LEN']):
					if word in package['keys'][i]:
						print package['keys'][i]
						ttt=ttt+1
						tot=tot+1
						page={}
						page['id']=tot
						page['title']=package['title'][i]
						page['link']=package['link'][i]
						page['summaryLess']=package['summaryLess'][i]
						page['linkPos']=package['linkPos'][i]
						if  package['summaryLess'][i]!=package['summary'][i]:
							page['has_more']=True
							page['summary']=package['summary'][i]
						else:
							page['has_more']=False
						if (l<=tot) and (tot<=r):
							pages.append(page)
	
				print 'find tot :',ttt
	
	#make info
	alll = (tot-1)/10+1
	if (pageId>0):
	#	print 'page_previous:',1,' ',pageId-1
		info['page_previousId']=pageId-1
		info['page_previous']=[]
		for x in range(1,pageId-1+1):
			info['page_previous'].append(x);
	if (r<tot):
	#	print 'page_next:',pageId+1,' ',alll
		info['page_nextId']=pageId+1
		info['page_next']=[]
		for x in range(pageId+1,alll+1):
			info['page_next'].append(x);
	info['page_index']=pageId
	info['myindex']=myindex
	info['where']=where
	


	return render(request,'search.html',{'word':word,'pages':pages,'info':info})


def to_notfound(request):
	print '%s redirectto notfound' %request.path
	return HttpResponseRedirect('/notfound')
	
def login(request):
	return render(request,'login.html')

def register(request):
	return render(request,'register.html')
	
def base(request):
	return render(request,'__base__.html')
	