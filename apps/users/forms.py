# -*- coding:utf-8 -*-
#date:

from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)


class RegisterForm(forms.Form):
    email = forms.CharField(required=True)
    password = forms.CharField(required=True)
    ##验证码
    captcha = CaptchaField()


