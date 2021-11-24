from django import forms
class StudentRegistration(forms.Form):
    name=forms.CharField() 
    email=forms.EmailField()  
    password=forms.CharField(widget=forms.PasswordInput,required=True) 
    #1
    def clean_name(self):  # for specific field
        valname=self.cleaned_data['name']
        if len(valname) < 3:
            raise forms.ValidationError('Enter more then 3 char')
        return valname
    #2
    def clean(self): # for whole form custom validation
        cleaned_data = super().clean() # it means parent class validation bhi work krega(will work)
        ename=self.cleaned_data['name']
        eemail=self.cleaned_data['email']
        passw=self.cleaned_data['password']
        
        if len(ename) >15:
            raise forms.ValidationError('Name shoud be equal or less then 15')
        
        if eemail != 'anamika@gmail.com':
            raise forms.ValidationError('Incorrect Mail')
        
        if len(passw) <8:
            raise forms.ValidationError('Password shoud be equal or greater then 8')
        
        
        