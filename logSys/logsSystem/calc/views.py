from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Home.html', {'name':'Ali'})

def add(request):
    
    num1 = request.POST['num1']
    num2 = request.POST['num2']

    sum = int(num1) + int(num2)
    return render(request, 'Results.html', {'result': sum})