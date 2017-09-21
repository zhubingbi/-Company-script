# coding:utf-8
from django import forms


class Register(forms.Form):
    name = forms.CharField(max_length=32, label='姓名')
    # required=false 代表输入可以为空
    gender = forms.CharField(label='性别')
    age = forms.IntegerField(label='年龄')
    height = forms.FloatField(label='身高')
    job = forms.CharField(max_length=32, label='工作',required=False)
    # required=false 代表输入可以为空
    money = forms.IntegerField(label='收入', required=False)


    def clean_name(self): #这个方法是在重写，函数名是固定的clean_filedName
        # 这个东西主要是验证name 首字母是不是字母。
        name = self.cleaned_data['name']
        if name[0].isalpha():
            return name
        else:
            raise forms.ValidationError('The first must be character')
        return name

    def clean_gender(self):
        # 自定义form验证
        gender = self.cleaned_data['gender']
        if gender in ['男'.decode('utf-8'), '女'.decode('utf-8')]:
            return gender
        else:
            raise forms.ValidationError('What are you gender')