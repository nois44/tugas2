from django import forms
from .models import Task


class TaskEditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['user']


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['is_finished', 'user']