from django import forms
from .models import User


class NewUserForm(forms.ModelForm):
    # name = forms.CharField()
    # email = forms.EmailField()
    # password = forms.PasswordInput()
    # verify_password = forms.PasswordInput()
    # text = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = User
        fields = '__all__'
