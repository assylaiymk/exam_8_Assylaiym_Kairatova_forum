from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from accounts.models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label_suffix='Login')
    password = forms.CharField(required=True, label='Password',
                               widget=forms.PasswordInput)
    next = forms.CharField(required=False, widget=forms.HiddenInput)


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Confirm password', strip=False, required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password', 'password_confirm', 'first_name', 'last_name', 'email')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise ValidationError('Password is not the same')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        user.groups.add('user')

        if commit:
            user.save()
            user.profile = Profile.objects.get_or_create(user=user)
        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email')
        labels = {'first_name': 'Name', 'Last_name': 'Surname', 'email': 'Email', }


class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'birthday')
