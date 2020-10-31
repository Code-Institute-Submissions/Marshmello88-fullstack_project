from django import forms
from .models import Order, PromoCode


class OrderForm(forms.ModelForm):
    promo_code = forms.CharField(required=False)

    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county', 'promo_code')

    def clean_promo_code(self):
        code = self.cleaned_data['promo_code']
        if not code:
            return None
        if not self.user.is_authenticated:
            return None

        try:
            promo_code = PromoCode.objects.get(code=code, user=self.user, used_at__isnull=True)
            return promo_code
        except PromoCode.DoesNotExist:
            raise forms.ValidationError('This code is invalid')


    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
            'promo_code': 'Your promo code',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = ''
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                elif field in placeholders:
                    placeholder = placeholders[field]
                if placeholder:
                    self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False