"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app.models import serviceprovider,Servicebooking,Payment
class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
class ServiceProviderForm(forms.ModelForm):
    class Meta:
        model=serviceprovider
        exclude=['verification_status']
       
class ServiceBookingForm(forms.ModelForm):
    class Meta:
        model=Servicebooking
        #fields='__all__'
        fields=['username','typeofservicereq','fromdate','todate','sp_id','sp_name','servicecharge','address_remarks']
        widgets={
            'typeofservicereq':forms.TextInput({
                                   'class': 'form-control'
                                   }),
            'fromdate': forms.TextInput({
                                   'class': 'form-control'
                                   }),
             'todate': forms.TextInput({
                                   'class': 'form-control'
                                   }),
             'sp_id':forms.NumberInput({
                                   'class': 'form-control'
                                   }),
             'sp_name':forms.TextInput({
                                   'class': 'form-control'
                                   }),
             'servicecharge':forms.NumberInput({
                                   'class': 'form-control'
                                   }),
             'address_remarks':forms.Textarea({
                                   'class': 'form-control'
                                   })

            }

class ServiceApproveForm(forms.ModelForm):
    class Meta:
        model=Servicebooking
        fields=['username','typeofservicereq','fromdate','todate','sp_name','servicecharge','total_days','sbapproval','total_amount',]

class PaymentForm(forms.ModelForm):
    class Meta:
        model=Payment
        fields="__all__"


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2','first_name','last_name','email'] 
 



'''
      widgets={
            'username':forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder':'Enter username'}),
            'password1':forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Enter Password'}),
            'password2':forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Enter Confirm Password'}),
             
            }
'''
 