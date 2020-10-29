from django import forms

from home.models import NewsletterSignup

class NewsletterSignupForm(forms.ModelForm):

    class Meta:
        model = NewsletterSignup
        fields = ['email']