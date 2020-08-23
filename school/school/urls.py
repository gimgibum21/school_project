"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from dongsugong.views import main
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name="main"),
    path('grade/', include('grade.urls')),
    path('upload/', include('upload.urls')),
    path('Update/', include('Update.urls', namespace="Update")),
    path('Details/', include('Details.urls')),
    path('G1subject/', include('G1subject.urls')),
    path('G2subject/', include('G2subject.urls')),
    path('G3subject/', include('G3subject.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
