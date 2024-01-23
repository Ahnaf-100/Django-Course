from typing import Any
from django import forms
from django.core import validators


# widgets = field to HTML input
class contactForm(forms.Form):
    name = forms.CharField(label="Fullname :", help_text="Total length must be 70 characters", required=False, widget=forms.Textarea(attrs={'id': 'text_area', 'class' : 'class1 class2','placeholder': 'Enter your name'}))
    # file = forms.FileField()
    email = forms.EmailField(label="User Email")
    # Age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    age = forms.CharField(widget=forms.NumberInput)
    check = forms.BooleanField()
    # birthday = forms.DateField()
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}))
    appoinment = forms.DateTimeField(widget=forms.DateInput(attrs={'type' : 'datetime-local'}))
    CHOICES = [('S', 'Small',), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    OPTIONS = [('P', 'Pepperoni'),('M', 'Mashroom'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices=OPTIONS, widget=forms.CheckboxSelectMultiple)


# class Studentdata(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Enter a name with at least 10 characters")
    #     return valname

    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Your email miust contain .com")
    #     return valemail

    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
    #     if len(valname) < 10:
    #          raise forms.ValidationError("Enter a name with at least 10 characters")
    #     if '.com' not in valemail:
    #          raise forms.ValidationError("Your email miust contain .com")


class Studentdata(forms.Form):
    name = forms.CharField(widget=forms.TextInput, validators=[validators.MaxLengthValidator(10, message="Enter an a amae with at max 10 characters")])
    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message="Enter a valid email")])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(34, message="age must be maximum 34"),validators.MinValueValidator(24, message="age must be munumum 24")])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'], message="File extension must be ended with .pdf")])


class PasswordValidatioProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']

        if val_conpass != val_pass:
            raise forms.ValidationError("password doesn't match")
        if len(val_name) < 15:
            raise forms.ValidationError("Name must be at least 15 characters")