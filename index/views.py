﻿from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import article
def index(request):
    return HttpResponse(u'''hello world<br>
    	<a href = 'list'>list</a><br>
    	<a href = 'main'>main</a><br>

    	''')
def list(request):
	alist = ['one', 'two', 'three']
	return render(request, 'list.htm', {'testlist': alist})
def main(request):
	class wz(object):
		def __init__(self, title='title', date='1970/1/1', contents='balablashenmade'):
			self.title = title
			self.date = date
			self.contents = contents
	a1 = wz('wo shi yi')
	a2 = wz()
	a3 = wz(date='2012/12/21')
	articlelist = [a1, a2, a3]
	#article.objects.create(title = '111', content = 'biubiubiu')
	articlelist = article.objects.all()
	return render(request, 'main.htm',{'articlelist': articlelist})
