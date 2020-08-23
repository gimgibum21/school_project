from django.shortcuts import render
from dongsugong.models import DSG

# Create your views here.


def show(request, spray_id):
    spray = DSG.objects.get(pk=spray_id)
    context = {
        'spray': spray
    }
    return render(request, 'Details/show.html', context)
