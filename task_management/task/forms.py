from django import forms
from . import models

class TaskForm(forms.ModelForm):
    class Meta:
        model = models.taskModel
        fields = '__all__'

        widgets = {
            'taskAssignDate': forms.DateInput(
                attrs={'type': 'date'},
                format='%Y-%m-%d'
            )
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['taskAssignDate'].input_formats = ['%Y-%m-%d']
