from django import forms
from .models import Task

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write the title of your task'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write the description of your task'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'})
        }

class GetTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']