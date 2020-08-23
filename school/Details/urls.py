from django.urls import path
from .views import show


app_name = "Details"
urlpatterns = [
    path('show/<int:spray_id>/', show, name="show")
]
