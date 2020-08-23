from django.urls import path
from .views import edit, edit2, delete

app_name = "Update"
urlpatterns = [
    path('edit/<int:spray_id>/', edit, name="edit"),
    path('edit2/<int:spray_id>/', edit2, name="edit2"),
    path('delete/<int:spray_id>', delete, name="delete"),
]
