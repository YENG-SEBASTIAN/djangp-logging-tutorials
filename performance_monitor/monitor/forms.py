# forms.py
from django import forms


class UserPasswordResetForm(forms.Form):
    password = forms.CharField(
        max_length=255, widget=forms.PasswordInput(attrs={'placeholder': 'New Password'})
    )
    password2 = forms.CharField(
        max_length=255, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})
    )

    def __init__(self, *args, **kwargs):
        self.uid = kwargs.pop('uid', None)
        self.token = kwargs.pop('token', None)
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data
