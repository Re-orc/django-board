from django import forms
from .models import Board
from django.contrib.auth.models import User

class noticeForm(forms.ModelForm):
    file = forms.FileField(required=False)
    class Meta:
        model = Board
        fields = ('title','text','file')

class ResiterForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email',)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('패스워드가 틀렸습니다.')
        return cd['password2']
