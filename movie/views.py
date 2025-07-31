from django.shortcuts import render
from django.http import HttpResponse

 # Create your views here.
def home(request):
    return render (request, 'home.html', {'name': 'Sara'})
def about(request):
    return HttpResponse("About Movie Reviews: This is a platform to share and read movie reviews.")