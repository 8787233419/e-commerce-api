from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def front(request) :
#     return render(request, '#the html file')

# Instead of a html file (dne till now) so instead a http response
def taskList(request) : 
    return HttpResponse('Ok?')