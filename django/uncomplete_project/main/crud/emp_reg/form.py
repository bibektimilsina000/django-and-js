from django import forms
from .models import Employee



class Emp_form(forms.ModelForm):
        class Meta:
            model=Employee
            fields='__all__'

