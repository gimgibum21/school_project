from django.urls import path
from .views import physics2, chemistry2, biologics2

app_name = "G3subject"
urlpatterns = [
    path('physics2/', physics2, name="physics2"),
    path('chemistry2/', chemistry2, name="chemistry2"),
    path('biologics2/', biologics2, name="biologics2"),
]
