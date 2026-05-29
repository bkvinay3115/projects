"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app.models import serviceprovider, Servicebooking, Payment


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses bootstrap CSS."""

    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'User name'
            }
        )
    )

    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        )
    )


class ServiceProviderForm(forms.ModelForm):
    class Meta:
        model = serviceprovider
        exclude = ['verification_status']


class ServiceBookingForm(forms.ModelForm):
    class Meta:
        model = Servicebooking

        fields = [
            'username',
            'typeofservicereq',
            'fromdate',
            'todate',
            'sp_id',
            'sp_name',
            'servicecharge',
            'address_remarks'
        ]

        widgets = {
            'typeofservicereq': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'fromdate': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'todate': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'sp_id': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'sp_name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'servicecharge': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'address_remarks': forms.Textarea(
                attrs={'class': 'form-control'}
            ),
        }


class ServiceApproveForm(forms.ModelForm):
    class Meta:
        model = Servicebooking

        fields = [
            'username',
            'typeofservicereq',
            'fromdate',
            'todate',
            'sp_name',
            'servicecharge',
            'total_days',
            'sbapproval',
            'total_amount',
        ]


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'email'
        ]
