from django.contrib import admin
from .models import DSG

# Register your models here.


@admin.register(DSG)
class DSGadmin(admin.ModelAdmin):
    list_display = (
        'id',
        'grade',
        'subject',
        'title',
        'created_at',
        'updated_at',
        'image',
    )
    search_fields = (
        'title',
    )
