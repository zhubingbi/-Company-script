# coding=utf-8

from django import forms
class AdminUserForm(forms.Form):
    phone = forms.CharField(max_length=32, label='注册电话', widget=forms.TextInput(attrs={'class': 'form-control'}))
    user = forms.CharField(max_length=32, label='用户名称', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=32, label='用户密码', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='注册邮箱', required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    isadmin = forms.IntegerField(label='用户权限', widget=forms.TextInput(attrs={'class':'form-control'}))
    photo = forms.ImageField(label='用户头像', required=False)


