from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from task.models import Task
from django.utils import timezone
from django.shortcuts import redirect

# Create your views here.

def index(request):
	if request.method == 'GET':
		import os
		os.chdir('media')
		os.system('rm * -f')
		os.chdir('..')
		return render(request,'task/index.html')
	elif request.method == 'POST':
		t =  request.POST.get("music", "")
		print t
		import os
		import glob
		from bs4 import BeautifulSoup
		import urllib2

		search = 'love story taylor' #I love you Taylor swift!
		search = str(t)
		search = search.replace(' ','%20')

		print('Making a Query Request! ')
		response = urllib2.urlopen('https://www.youtube.com/results?search_query='+search)
		html = response.read()
		soup = BeautifulSoup(html, 'html.parser')
		for link in soup.find_all('a'):
		    if '/watch?v=' in link.get('href'):
		    	print(link.get('href'))
		    	# May change when Youtube Website may get updated in the future.
		    	proper_linl = link.get('href')
		    	break
		 
		proper_linl =  'http://www.youtube.com/'+proper_linl
		print os.system('cd media/')
		print (os.system)
		command = 'youtube-dl --extract-audio --audio-format mp3 -o "media/%(title)s.%(ext)s" '+proper_linl
		print command
		print ('Processed Querying , Starting Phase 2')
		os.system(command)
		return redirect('/downloaded')

def downloaded(request):
	if request.method == 'GET':
		import os
		import glob
		os.chdir('media')
		for file in glob.glob("*.mp3"):
			loc = file
	print loc
	context = {'file':'/media/'+loc}
	os.chdir('..')	
	return render(request,'task/finished.html',context)		
