from django import forms
from crm.models import Mobile
from django.contrib.auth.models import User


# class MobileForm(forms.Form):
    
#     name=forms.CharField(widget=forms.TextInput(attrs={"class":'form-control'}))

#     brand=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

#     price=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))

#     RAM=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

#     color=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

#     picture=forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))

class MobileForm(forms.ModelForm):
    class Meta:
        model=Mobile
        fields="__all__"


class SignUpForm(forms.ModelForm):
    class Meta:
            model=User
            fields=["username","email","password"]

class SignInForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)     

class MobileUpdateForm(forms.ModelForm):
     class Meta:
        model=Mobile
        fields="__all__"
        widgets={


        }
