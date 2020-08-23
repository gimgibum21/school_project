from django.shortcuts import render
from dongsugong.models import DSG

# Create your views here.


def physics2(request):
    context = {
        'sprayT': DSG.objects.filter(grade="3학년", subject="물2"),
    }
    return render(request, 'G3subject/physics2.html', context)


def chemistry2(request):
    context = {
        'sprayT': DSG.objects.filter(grade="3학년", subject="화2"),
    }
    return render(request, 'G3subject/chemistry2.html', context)


def biologics2(request):
    context = {
        'sprayT': DSG.objects.filter(grade="3학년", subject="생2"),
    }
    return render(request, 'G3subject/biologics2.html', context)
