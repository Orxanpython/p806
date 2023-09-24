from django import forms
from core.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'email-bt', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'email-bt', 'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'class': 'email-bt', 'placeholder': 'Message'}),
        }


#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
        
       
#         self.fields['name'].widget.attrs['placeholder'] = 'Your Name'
#         self.fields['email'].widget.attrs['placeholder'] = 'Your Email'
#         self.fields['message'].widget.attrs['placeholder'] = 'Your Message'
