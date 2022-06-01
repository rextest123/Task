from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class':'form__input',
            'placeholder' : 'Введите телефон'
        }),
            "task": Textarea(attrs={
                'class':'form__label',
                'placeholder': 'Введите описание'
            })
        }
