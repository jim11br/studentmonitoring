from django.db import models  
from django.forms import fields  
from .models import *  
from django import forms

class ImageForm(forms.ModelForm):
    class Meta:
        model = FaceImage
        fields = '__all__'