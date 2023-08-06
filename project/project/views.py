from django.shortcuts import render
from django.http import HttpResponse

def base_file(request):
 	return render(request,'base.html')