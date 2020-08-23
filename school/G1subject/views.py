from django.shortcuts import render
from dongsugong.models import DSG

# Create your views here.


def SR(request):
    context = {
        'sprayT': DSG.objects.filter(grade="1학년", subject="과학탐구"),
    }
    return render(request, 'G1subject/SR.html', context)


def art(request):
    context = {
        'sprayT': DSG.objects.filter(grade="1학년", subject="미술"),
    }
    return render(request, 'G1subject/art.html', context)


def PE(request):
    context = {
        'sprayT': DSG.objects.filter(grade="1학년", subject="체육"),
    }
    return render(request, 'G1subject/PE.html', context)


