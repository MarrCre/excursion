from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'name':'Excursion'}
    return render(request, r'main\index.html', context)