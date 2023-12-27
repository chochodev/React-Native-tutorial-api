from django.shortcuts import render
from django.http import HttpResponse

def home(self, request):
  if request.method == 'GET':
    
    return HttpResponse("Hello from get home view!")

  return HttpResponse("Hello from the home view!")

def jobs(self, request):

  return None