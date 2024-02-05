from django.shortcuts import render
from django.http.response import HttpResponse


context = {
    "title" : "Home page"
}

def index(request):
    return render(request, 'web/index.html', context=context)
