from django import forms
from django.core import validators

class FeedbackForm(forms.Form):
    name=forms.CharField()
    village=forms.CharField()
    mandal=forms.CharField()
    district=forms.CharField()
    phonenumber=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)

def clean(self):
    print('Total Form Validation by using single clean method...')
    total_cleaned_data=super().clean()
    if inputrollno<=0:
        raise forms.ValidationError('Rollno should be >0')
    inputname=total_cleaned_data['name']  
    inputvillage=total_cleaned_data['village']
    inputmandal=total_cleaned_data['mandal']
    inputdistrict=total_cleaned_data['district']
    inputphone=total_cleaned_data['phonenumber']
    if len(inputphone)<=9:
        raise forms.ValidationError("Please enter valid phone number")
    if len(inputphone)>10:
        raise forms.ValidationError("Please enter valid Phone Number")
    inputemail=total_cleaned_data['email']
    if len(inputemail)<9:
        raise forms.ValidationError('Please enter the valid Emailid') 
    inputfeedback = total_cleaned_data['feedback']