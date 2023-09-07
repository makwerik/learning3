from django.forms import ModelForm, TextInput, Textarea
from.models import *


class AddPost(ModelForm):
    class Meta:
        model = Women
        fields = ['title', 'content']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            })
        }
