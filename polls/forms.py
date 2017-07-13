from django import forms
from django.contrib.auth.models import User
from polls.models import Question, Choice, UserProfile



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class UserProfileForm(forms.ModelForm):
    username = forms.CharField()
    address = forms.CharField()

    #def clean_email()
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'address',
        )