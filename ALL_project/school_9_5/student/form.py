# coding:utf-8
from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=32, label='姓名',widget=forms.TextInput(attrs={'class':'form-control'}))
    gender = forms.CharField(max_length=32, label='性别',widget=forms.TextInput(attrs={'class':'form-control'}))
    age = forms.IntegerField(label='年龄',widget=forms.TextInput(attrs={'class':'form-control'}))
    birthday = forms.DateTimeField(label='生日',widget=forms.TextInput(attrs={'class':'form-control'}))
    grade = forms.CharField(max_length=32, label='班级',widget=forms.TextInput(attrs={'class':'form-control'}))
    subject = forms.CharField(max_length=32, label='专业',widget=forms.TextInput(attrs={'class':'form-control'}))
    city = forms.CharField(max_length=32, label='城市',widget=forms.TextInput(attrs={'class':'form-control'}))