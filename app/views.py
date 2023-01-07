from django.shortcuts import render

# Create your views here.

def some(request):
    return render(request,'some.html')