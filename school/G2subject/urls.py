from django.urls import path
from .views import math1, math2, english

app_name = "G2subject"
urlpatterns = [
    path('math1', math1, name="math1"),
    path('math2', math2, name="math2"),
    path('english', english, name="english"),
]
