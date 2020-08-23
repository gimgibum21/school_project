from django.urls import path
from .views import SR, art, PE

app_name = "G1subject"
urlpatterns = [
    path('SR/', SR, name="SR"),
    path('art/', art, name="art"),
    path('PE/', PE, name="PE"),
]
