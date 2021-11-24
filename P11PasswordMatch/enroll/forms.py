from django import forms
class StudentRegistration(forms.Form):
    name=forms.CharField() 
    email=forms.EmailField()  
    password=forms.CharField(widget=forms.PasswordInput) 
    confirm_password=forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        cleaned_data=super().clean()
        npass=self.cleaned_data['password']
        cpass=self.cleaned_data['confirm_password']
        
        if npass != cpass:
            raise forms.ValidationError('Password and confirm password Should be same')
        return cleaned_data
    