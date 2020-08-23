from django.shortcuts import render
from dongsugong.models import DSG

# Create your views here.


def math1(request):
    context = {
        'sprayT': DSG.objects.filter(grade="2학년", subject="수1"),
    }
    return render(request, 'G2subject/math1.html', context)


def math2(request):
    context = {
        'sprayT': DSG.objects.filter(grade="2학년", subject="수2"),
    }
    return render(request, 'G2subject/math2.html', context)


def english(request):
    context = {
        'sprayT': DSG.objects.filter(grade="2학년", subject="영어"),
    }
    return render(request, 'G2subject/english.html', context)
