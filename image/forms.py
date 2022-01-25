from django import forms
# from .models import ImageProfile
from .models import inputmodel

# class imageForm(forms.ModelForm):

#     class Meta:
#         model = ImageProfile
#         fields = ['images']

class inputForm(forms.ModelForm):

    class Meta:
        model = inputmodel
        fields = '__all__'