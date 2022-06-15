from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'createform',
                'placeholder': 'Название статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'createform',
                'placeholder': 'Описание'
            }),
            "date": DateTimeInput(attrs={
                'class': 'createform',
                'placeholder':'Дата'
            }),
            "full_text": Textarea(attrs={
                'class': 'createform',
                'placeholder': 'Текст'
            })

        }