from django import forms
from .models import DSG


class DSGform(forms.ModelForm):
    class Meta:
        model = DSG
        fields = [
            'title',
            'content',
            'image',
        ]

        labels = {
            'title': '제목',
            'content': '내용',
            'image': '수행평가 사진',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control'
            }),
        }
