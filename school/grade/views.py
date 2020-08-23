from django.shortcuts import render

# Create your views here.


def first(request):
    return render(request, 'grade/first.html')


def second(request):
    return render(request, 'grade/second.html')


def third(request):
    return render(request, 'grade/third.html')
