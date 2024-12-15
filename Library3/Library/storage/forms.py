from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title','avtor','idnumber','vidan','vrem']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название книги'
            }),
            "avtor": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ф.И.О Автора'
            }),
            "idnumber": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер книги'
            }),
            "vidan": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Кому выдана'
            }),
            "vrem": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Время выдачи'
            })
            
        }