from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'name':'Excursion'}
    retrun render(request, 'excursion\main\templates\main\index.html', context)