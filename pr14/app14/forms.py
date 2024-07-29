from django .forms import fields
from .models import employee
from django import forms

class employeeform(forms.ModelForm):  
  
    class Meta:  
        # To specify the model to be used to create form  
        model = employee  
        # It includes all the fields of model  
        fields = '__all__'  