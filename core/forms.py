from django import forms
from core.models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'email-bt', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'email-bt', 'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'class': 'email-bt', 'placeholder': 'Message'}),
        }




class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'country', 'address', 'town_city', 'country_state', 'postcode', 'phone', 'email', 'account_password', 'order_notes']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'checkout__input', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'checkout__input', 'placeholder': 'Last Name'}),
            'country': forms.TextInput(attrs={'class': 'checkout__input', 'placeholder': 'Country'}),
            'address': forms.TextInput(attrs={'class': 'checkout__input', 'placeholder': 'Address'}),
            'town_city': forms.TextInput(attrs={'class': 'checkout__input', 'placeholder': 'Town/City'}),
            'country_state': forms.TextInput(attrs={'class': 'checkout__input', 'placeholder': 'Country/State'}),
            'postcode': forms.TextInput(attrs={'class': 'checkout__input', 'placeholder': 'Postcode / ZIP'}),
            'phone': forms.TextInput(attrs={'class': 'checkout__input', 'placeholder': 'Phone'}),
            'email': forms.EmailInput(attrs={'class': 'checkout__input', 'placeholder': 'Email'}),
            'account_password': forms.PasswordInput(attrs={'class': 'checkout__input', 'placeholder': 'Account Password'}),
            'order_notes': forms.Textarea(attrs={'class': 'checkout__input', 'placeholder': 'Order Notes'}),
        }

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
        
       
#         self.fields['name'].widget.attrs['placeholder'] = 'Your Name'
#         self.fields['email'].widget.attrs['placeholder'] = 'Your Email'
#         self.fields['message'].widget.attrs['placeholder'] = 'Your Message'
