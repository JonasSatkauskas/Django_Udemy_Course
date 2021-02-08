from django import forms

class FormUser(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.PasswordInput()
    verify_password = forms.PasswordInput()
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        password = all_clean_data['password']
        verify_password = all_clean_data['verify_password']

        if password != verify_password:
            raise forms.ValidationError('MAKE SURE EMAILS MATCH!')
