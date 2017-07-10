from django import forms
from django.contrib.auth.models import User
from polls.models import Question, Choice, UserProfile



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('name', 'registration_id', 'address')