from django.shortcuts import render, redirect
from dongsugong.models import DSG
from dongsugong.forms import DSGform

# Create your views here.


def edit(request, spray_id):
    spray = DSG.objects.get(pk=spray_id)
    context = {
        'spray': spray,
        'form': DSGform(instance=spray)
    }
    return render(request, 'Update/edit.html', context)


def edit2(request, spray_id):
    if request.method == "POST" or request.method == "FILES":
        spray = DSG.objects.get(pk=spray_id)
        form = DSGform(request.POST, request.FILES or None, instance=spray)
        if form.is_valid():
            form.save()
        return redirect('Details:show',  spray_id)


def delete(request, spray_id):
    if request.method == "POST":
        spray = DSG.objects.get(pk=spray_id)
        spray.delete()
        return redirect('main')
