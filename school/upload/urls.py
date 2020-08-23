from django.urls import path
from .views import Upload, create


app_name = "upload"
urlpatterns = [
    path('upload/', Upload, name="upload"),
    path('create/', create, name="create"),
]
