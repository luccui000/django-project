from django import forms
from django.contrib.auth import get_user_model
from django.db import models


class ContactForm(forms.Form):
    fullname    = forms.CharField(
            widget = forms.TextInput(
                attrs = {
                    'class' : 'form-control' ,
                    'placeholder' : 'Your Name'
                    }
            )
        )
    email   = forms.EmailField(
        widget = forms.EmailInput(
            attrs = {
                'class' : 'form-control',
                'placeholder' : 'examples@gmail.com'
            }
        )
    )
    message = forms.CharField(
        widget = forms.Textarea(
            attrs = {
                'class' : 'form-message',
                'placeholder' :  'message'
            }
        )
    )
   
    # content = forms.CharField()
    def clean_email(self):
        email = self.cleaned_data.get("email")

        if not "gmail.com" in email:                               # kiem tra trong email gmail.com hay khong
            raise forms.ValidationError("Email khong hop le")      # neu email khong hop le thi thong bao lo
        return email



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget= forms.PasswordInput)

User  = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField(label="Ten dang nhap")
    email    = forms.EmailField()   
    password = forms.CharField(label="Mat Khau",widget= forms.PasswordInput)
    password2 = forms.CharField(label="Xac nhan Mat Khau",widget= forms.PasswordInput)


    def clean_username(self):
        username = self.cleaned_data.get("username")
        kiemtra  = User.objects.filter(username=username)
        if kiemtra.exists():
            raise forms.ValidationError("Ten da duoc su dung")
        return username
    def clean_email(self):
        email = self.cleaned_data.get("email")
        kiemtra  = User.objects.filter(email=email)
        if kiemtra.exists():
            raise forms.ValidationError("Email da duoc su dung")
        return email
    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password != password2:
            raise forms.ValidationError("Mat khau khong trung nhau")
        return data
