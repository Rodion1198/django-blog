from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, UserCreationForm


User = get_user_model()


class SingUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SingUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_login = forms.CharField(max_length=255, widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    is_superuser = forms.CharField(max_length=255, widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    is_staff = forms.CharField(max_length=255, widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    is_active = forms.CharField(max_length=255, widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    date_joined = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password', 'last_login', 'is_active',
                  'is_superuser', 'is_staff', 'date_joined')


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                     'type': 'password'}))
    new_password1 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                      'type': 'password'}))
    new_password2 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                      'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
