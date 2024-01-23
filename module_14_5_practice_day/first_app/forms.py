from django import forms
from first_app.models import MyModel

# from django.core import validators
# from django.forms.widgets import NumberInput
# import datetime

# BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']

# FAVORITE_COLORS_CHOICES = [
#     ('blue', 'Blue'),
#     ('green', 'Green'),
#     ('black', 'Black'),
# ]
# class ExampleForm(forms.Form):
#     name = forms.CharField(initial='Your name')
#     # name = forms.CharField(label="Fullname :", help_text="Total length must be 70 characters", required=False, widget=forms.Textarea(attrs={'id': 'text_area', 'class' : 'class1 class2','placeholder': 'Enter your name'}))
#     comment = forms.CharField(widget=forms.Textarea(attrs={'rows' : 3}), required=False)
#     email = forms.EmailField(label="Please enter your email address",)
#     agree = forms.BooleanField(initial=True)
#     date = forms.DateField()
#     birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
#     birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
#     message = forms.CharField(
# 	max_length = 10,
# )
#     value = forms.DecimalField()
#     day = forms.DateField(initial=datetime.date.today)
#     favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)

class ExampleForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = "__all__"