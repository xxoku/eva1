from django.shortcuts import render

# Create your views here.


def prueba1(request):
    data = []
    return render (request, 'app1/index.html')