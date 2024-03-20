from django import forms
from .models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['family', 'first_name', 'last_name', 'middle_name', 'birth_date', 'death_date',
                  'education', 'occupation', 'hobbies', 'photo', 'notes']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Name'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'death_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'education': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'occupation': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'hobbies': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }
        labels = {
            'family': 'Family',
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name
