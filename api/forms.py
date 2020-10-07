from django.forms import ModelForm, PasswordInput, CharField

from .models import *


class AccountForm(ModelForm):
    password = CharField(widget=PasswordInput())

    class Meta:
        model = Account
        fields = '__all__'

    def save(self, commit=True):
        account = super(AccountForm, self).save(commit=False)
        account.set_password(self.cleaned_data["password"])
        if commit:
            account.save()
        return account
