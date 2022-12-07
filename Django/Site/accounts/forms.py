from .models import Edit

from django.forms import ModelForm, Textarea, TextInput, NumberInput

class EditForm(ModelForm):
    class Meta:
        model = Edit
        fields = ['username', 'name', 'age', 'skills', 'job_places', 'money']
        widgets = {'username': TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Введите ваш логин (написан в верхнем правом углу)",
        }),'name': TextInput(attrs={
            'class': 'form-control',
            'placeholder': "ФИО"
        }),'age': NumberInput(attrs={
            'class': 'form-control',
            'min': '0', 'max': '10000000',
            'placeholder': "Возраст"
        }),'skills': Textarea(attrs={
            'class': 'form-control',
            'placeholder': "Навыки"
        }),'job_places': Textarea(attrs={
            'class': 'form-control',
            'placeholder': "Предыдущие рабочие места"
        }),'money': NumberInput(attrs={
            'class': 'form-control',
            'min': '0', 'max': '10000000',
            'placeholder': "Зарплатные ожидания"
        })}


    def __init__(self, lst=[], req=None):
        super().__init__()
        print(lst)
        if lst != []:
            self.fields['username'].initial = lst[0]
            self.fields['name'].initial = lst[1]
            self.fields['age'].initial = lst[2]
            self.fields['skills'].initial = lst[3]
            self.fields['job_places'].initial = lst[4]
            self.fields['money'].initial = lst[5]


