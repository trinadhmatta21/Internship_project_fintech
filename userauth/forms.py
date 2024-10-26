# userauth/forms.py
from django import forms
from .models import User, IPO
from django.contrib.auth.forms import SetPasswordForm

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['name', 'email', 'password']


class SignInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class IPOForm(forms.ModelForm):
    class Meta:
        model = IPO
        fields = [
            'company_logo',
            'company_name',
            'price_band',
            'open_date',
            'close_date',
            'issue_size',
            'issue_type',
            'listing_date',
            'status',
            'ipo_price',
            'listing_price',
            'listing_gain',
            'current_market_price',
            'current_return',
            'rhp_pdf',
            'drhp_pdf',
        ]


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        label="Registered Email",
        max_length=254,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your registered email'})
    )

