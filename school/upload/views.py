from django.shortcuts import render, redirect
from dongsugong.models import DSG

# Create your views here.


def Upload(request):
    return render(request, 'upload/upload.html')


def create(request):
    if request.method == "POST" or request.method =="FILES":
        grade = request.POST.get('grade')
        subject = request.POST.get('subject')
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        DSG(grade=grade, subject=subject, title=title, content=content, image=image).save()
        return redirect('main')
