from django import forms
from . models import Records

class RecordForm(forms.Form):
    first_name = forms.CharField(max_length=50, label="Name")
    last_name = forms.CharField(max_length=50, label="Last name")
    email = forms.CharField(max_length=50, label="Email")
    phone = forms.CharField(max_length=15, label="Phone")
    adress = forms.CharField(max_length=100, label="Adress")
    city = forms.CharField(max_length=50, label="City")
    state = forms.CharField(max_length=50, label="State")
    zipcode = forms.CharField(max_length=20, label="Zip code")

    def save(self):
        Records.objects.create(
            first_name = self.cleaned_data['first_name'],
            last_name = self.cleaned_data['last_name'],
            email = self.cleaned_data['email'],
            phone = self.cleaned_data['phone'],
            adress = self.cleaned_data['adress'],
            city = self.cleaned_data['city'],
            state = self.cleaned_data['state'],
            zipcode = self.cleaned_data['zipcode']
        )