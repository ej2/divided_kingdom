from django import forms
from django.contrib.auth import authenticate
from divided_kingdom.apps.core.patterns import PASSWORD


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=75, label="Email",
                             widget=forms.TextInput(attrs={"class": "span4", "maxlength": 75}))
    password = forms.RegexField(regex=PASSWORD, label="Password",
                                error_message="Please enter a valid password.",
                                widget=forms.PasswordInput(attrs={"class": "span4", "maxlength": 40}))

    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            self.user_cache = authenticate(email=email, password=password)

            if self.user_cache is None:
                raise forms.ValidationError(
                    "Please enter a correct email and password.")
            elif not self.user_cache.is_active:
                raise forms.ValidationError("This account is inactive.")

        return self.cleaned_data

    def get_user(self):
        return self.user_cache
