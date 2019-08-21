from django.shortcuts import render,redirect
from django.http import request
from pinax.documents.models import Folder,Document
import json
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
	return render(request,'home.html')

def searchmovie(request,search_text):
	# search_text=search_text.title()
	movies=Document.objects.filter(name__contains=search_text)
	mylist=[]
	for i in movies:
		mylist.append(i.name)
	print(mylist)
	mylist=json.dumps(mylist)
	return JsonResponse(mylist, safe=False)

def open_file(request,file_name):
	doc=Document.objects.get(name=file_name)
	print('doc_found')
	print(doc.id)
	url="/d/"+str(doc.id)
	return redirect(url)

